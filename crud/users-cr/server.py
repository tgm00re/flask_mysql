

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




if __name__ == "__main__":
    app.run(debug=True)