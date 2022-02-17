from crypt import methods
from flask_app.models.dojo import Dojo
from flask import request, redirect, render_template, session
from flask_app import app

@app.route('/')
def dojos():
    dojoList = Dojo.get_all()
    return render_template("dojos.html", dojoList=dojoList)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/display_dojos/<int:id>')
def display_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.dojo_with_ninjas(data)
    dojoName = dojo.name
    return render_template("display_single_dojo.html", dojoName=dojoName, dojo=dojo.ninjas, id=id)
