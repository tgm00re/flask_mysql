from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, render_template

class Dojo:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.location = data['location'],
        self.language = data['location'],
        self.comment = data['comment']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s"
        return connectToMySQL("dojo-survey").query_db(query, data)
    

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['email']) < 5:
            flash("Dojo Name Must be *5* or more characters")
            is_valid = False
        if  dojo['location'] == 'Choose...':
            flash("Please select a valid location")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("Language must be *2* or more characters")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Comment must be *10* or more characters")
            is_valid = False
        return is_valid
