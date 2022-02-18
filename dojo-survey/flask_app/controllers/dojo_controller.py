from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import dojo

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    if not dojo.Dojo.validate_dojo(request.form):
        return redirect('/')
    req = request.form
    session['email'] = req.get('email')
    session['password'] = req.get('password')
    session['address'] = req.get('address')
    session['second-address'] = req.get('second-address')
    session['city'] = req.get('city')
    session['location'] = req.get('state')
    session['zip'] = req.get('zip')
    session['newsletter'] = req.get('newsletter')
    session['language'] = req.get('language')
    return redirect('/display_information')

@app.route('/display_information')
def display_information():
    return render_template("display.html")