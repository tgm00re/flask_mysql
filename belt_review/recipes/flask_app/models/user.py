from pickle import TRUE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def save(self, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recipes').query_db(query, data)
        print("printing results")
        print(results)
        if len(results) < 1:
            return False #nobody w/ email
        return cls( results[0] )

    
    @staticmethod
    def validate_user(user):
        print("printing password")
        print(user['password'])
        print(str(len(user['password'])))
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be 2 or more characters", 'register')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be 2 or more characters", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email", 'register')
            is_valid = False
        if len(user['password']) < 3:
            flash("Passwords must be 3 or more characters", 'register')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match", 'register')
            is_valid = False
        return is_valid

        

    

