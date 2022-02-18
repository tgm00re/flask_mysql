from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import user
from flask_app.models import friendship

@app.route('/')
def root():
    #will need to get/pass-in info later
    friendships = user.User.get_friendships()
    users = user.User.get_all()
    return render_template('index.html', users=users, friendships=friendships)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name']
    }
    user.User.save(data)
    return redirect('/')

@app.route('/create_friendship', methods=['POST'])
def create_friendship():
    data = {
        "user_id": request.form['user_id'],
        "friend_id": request.form['friend_id']
    }
    if(not friendship.Friendship.check_for_friendship(data)):
        friendship.Friendship.save(data)
    return redirect('/')
    