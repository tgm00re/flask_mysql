from crypt import methods
from flask_app.models.ninja import Ninja
from flask import request, redirect, render_template, session
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/create_ninja')
def create_ninja():
    dojoList = Dojo.get_all()
    return render_template("create_ninja.html", dojoList=dojoList)

@app.route('/create_ninja_form', methods=['POST'])
def create_ninja_form():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojoID": request.form['dojoID'],
    }
    Ninja.save(data=data)
    return redirect('/')
