from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name'],
        self.description = data['description'],
        self.instructions = data['instructions'],
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at'],
        self.updated_at = data['created_at'],
        self.creator_id = data['creator_id'],
        self.made_on = data['made_on']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_thirty, created_at, updated_at, creator_id, made_on) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, NOW(), NOW(), %(creator_id)s, %(made_on)s);"
        return connectToMySQL('recipes').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return cls( result[0] )


    @classmethod
    def edit_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_thirty=%(under_thirty)s WHERE id = %(id)s"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL('recipes').query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        print("validating")
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters long" , 'create')
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Recipe description must be at least 3 characters long", 'create')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Recipe instructions must be at least 3 characters long", 'create')
            is_valid = False
        print("validation complete")
        return is_valid

