

from flask import Flask, render_template, redirect, request

from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    print('***- - - - - - - - - - - - - - - - - - - -')
    print(request.form["fname"])
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)
    return redirect('/display_users')

@app.route('/display_users')
def display_users():
    users = User.get_all()
    return render_template("display_users.html", users=users)

@app.route('/display_users/<int:id>')
def display_user(id):
    user = User.get_one(id)
    return render_template("display_single_user.html", user=user)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    return render_template('edit_user.html', id=id)

@app.route('/edit_user_call/<int:id>', methods=['POST'])
def edit_user_call(id):
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id": id
    }
    User.update(data)
    return redirect(f'/display_users/{id}')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/display_users')





if __name__ == "__main__":
    app.run(debug=True)