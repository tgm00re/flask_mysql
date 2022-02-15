from crypt import methods
from flask import Flask, redirect, render_template, request
#import the class from friend.py
from friend import Friend

app = Flask(__name__)

@app.route('/')
def index():
    #call the get all classmethod to get all the friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    #the insert queries return the id that's created, so, if you wanted, you could assign a variable to the function call to keep track of the new ID
    Friend.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)