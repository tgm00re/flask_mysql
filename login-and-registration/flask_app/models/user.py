from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import flash
import re
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.pw_hash = data['pw_hash'],
        self.user_level = data['user_level'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, user_level, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, %(user_level)s, NOW(), NOW() )"
        print("SAVING TO DB XD")
        return connectToMySQL('login-and-registration').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WhERE email = %(email)s"
        result = connectToMySQL('login-and-registration').query_db(query, data)
        if len(result) < 1: #Nobody in db
            return False
        return cls(result[0])


    @staticmethod
    def validate_user(user):
        is_valid = True
        if not user['first_name'].isalpha() or len(user['first_name']) < 1:
            flash("First Name Must Be Alphabetic And Not Left Empty!" ,'register')
            is_valid = False
        if not user['last_name'].isalpha() or len(user['last_name']) < 1:
            flash("Last Name Must Be Alphabetic And Not Left Empty!", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("pls input a valid email address", 'register')
            is_valid = False
        if len(user['password']) < 5:
            flash("passwords must be 5 or more characters", 'register')
        if user['password'] != user['confirm_password']:
            flash("Your passswords don't match...", 'register')
            is_valid = False
        return is_valid

