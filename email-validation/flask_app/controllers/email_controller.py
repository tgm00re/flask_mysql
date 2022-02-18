from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import email

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/create_email', methods=['POST'])
def create_email():
    if not email.Email.validate_email(request.form):
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    email.Email.save(data)
    return redirect('/display')

@app.route('/display')
def display():
    emails = email.Email.get_all()
    return render_template('display.html', emails=emails)

@app.route('/delete_email/<int:id>')
def delete_email(id):
    data = {
        "id": id
    }
    email.Email.delete(data)
    return redirect('/display')