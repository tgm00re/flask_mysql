import bcrypt
from flask import redirect, render_template, session, request, flash
from flask_app import app
from flask_app.models import user, recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register_user', methods=['POST'])
def register_user():
    if not user.User.validate_user(request.form):
        return redirect('/')
    if user.User.get_by_email({ "email": request.form['email'] } ):
        flash("Email already exists", 'register')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    } 
    user_id = user.User.save(data)
    session['user_id'] = user_id
    session['user_first'] = data['first_name']
    return redirect('/dashboard')

@app.route('/login_user', methods=['POST'])
def login_user():
    print(request.form)
    user_in_db = user.User.get_by_email({ "email": request.form['email'] })
    if not user_in_db:
        flash("Incorrect email/password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password[0], request.form['password']):
        flash("Incorrect email/password", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['user_first'] = user_in_db.first_name
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    recipes = recipe.Recipe.get_all()
    return render_template("dashboard.html", recipes=recipes)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
