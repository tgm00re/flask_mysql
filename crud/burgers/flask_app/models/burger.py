from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO restaurants ( name , bun, meat, calories, restaurant_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db =  connectToMySQL('burgers').query_db(query)
        burgers =[]
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('burgers').query_db(query,data)

        return cls(burger_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)


    @staticmethod #static because it's loosely related to the class, but doesn't give the class functionality
    def validate_burger(burger):
        is_valid = True #Assume it's valid at first
        if len(burger['name']) < 3:
            flash("Name must be at at least 3 characters.") #Flash messages are strings that exist for just one redirect cycle. Flash uses ssion so that we "Flash" our error messages on the form page. The difference betweeen fllash and session is that flash messages only last for one redirect while session stays until it is manually popped. This makes flash perfect for validations! WE NEED TO IMPOR FLASH AND SET UP SESSION IN OUR __init__.py (not in this folder, in flask_app) d
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calroies must be 200 or greater")
        if len(burger['meat']) < 3:
            flash("bun must be at least 3 characters.")
            is_valid = False
        return is_valid
