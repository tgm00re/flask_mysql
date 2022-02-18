from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask import render_template, redirect, request, flash,  session
bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/register_user', methods=['POST'])
def register_user():
    if not user.User.validate_user(request.form):
        return redirect('/')
    #create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    #Put the hash (and other data) into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "pw_hash": pw_hash,
        "user_level": int(request.form['user_level'])
    }
    emailData = { "email": request.form['email'] }
    if user.User.get_by_email(emailData):
        flash("email already exists", 'register')
        return redirect('/')
    user.User.save(data)
    return redirect('/')


@app.route('/login_user', methods=['POST'])
def login_user():
    #Check if user email in DB
    data = { "email": request.form["email"]}
    user_in_db = user.User.get_by_email(data) #returns a boolean or a user instance
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect('/')

    #check the password to see if it matches the user pwhash
    print(request.form['password'])
    print(user_in_db.pw_hash)
    if not bcrypt.check_password_hash(user_in_db.pw_hash[0], request.form['password']):
        flash("Invalid Email/Password (password)", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['user_level'] = user_in_db.user_level
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')
    