from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    #Inserts a dojo into the DB
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES( %(name)s, NOW(), NOW() );"
        return connectToMySQL('dojos-and-ninja').query_db(query, data)

    #Gets all dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        #returns list of dictionaries for all dojos
        result = connectToMySQL('dojos-and-ninja').query_db(query)
        #create list to append instances of dojo created
        dojos = []
        #iterate over list returned from result
        for dojo in result:
            #create a Dojo and append it to the list
            dojos.append( cls(dojo) )
        #return a list of dojo objects.
        return dojos

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL('dojos-and-ninja').query_db(query, data)
        return cls(result[0])

    @classmethod
    def dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s"
        results = connectToMySQL('dojos-and-ninja').query_db(query, data)
        dojo = cls( results[0] ) #We know the first (and ever) dojo will be the dojo w/ the riight id
        print("PRINTING DOJO: ")
        print(dojo.name)
        #now we parse the ninja data to make instances of ninjas and add them into our list
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data))
        print("printing again..")
        print(dojo.ninjas)
        return dojo



