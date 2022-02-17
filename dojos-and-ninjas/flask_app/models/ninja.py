from types import ClassMethodDescriptorType
from flask_app.config import mysqlconnection
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.age = data['age'],
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #dojo id?

    #returns a list of ninjas (all of them...Party Time!)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        result = connectToMySQL('dojos-and-ninja').query_db(query)
        ninjaList = []
        for ninja in result:
            ninjaList.append( cls(ninja) )
        return ninjaList

    #create a ninja!!
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES( %(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojoID)s)"
        return connectToMySQL('dojos-and-ninja').query_db(query, data)
        
    


