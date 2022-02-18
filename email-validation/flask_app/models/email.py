from unittest import result
from flask import flash
import re #Import regex module
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Will return an instance, so for regex check we check to see if nothing was returned
class Email:
    def __init__(self, data):
        self.id = data['id'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW() );"
        return connectToMySQL('emails').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('emails').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL('emails').query_db(query, data)


    @staticmethod
    def validate_email(email):
        print("Validating...")
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid E-mail Address", 'error')
            is_valid = False
        check_query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL('emails').query_db(check_query, email)
        print("PRINTING RESULTS: ")
        if results != ():
            flash("E-mail already in use! :(", 'error')
            is_valid = False
        if(is_valid):
            flash("Congratulations! You successfully typed in an e-mail address! I'm so proud of you!", 'success')
        return is_valid
