from tabnanny import check
from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    def __init__(self, data):
        self.user_id = data['user_id'],
        self.friend_id = data['friend_id']
    


    @classmethod
    def save(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        cls.check_for_friendship(data)
        return connectToMySQL('friendships').query_db(query, data)


    @classmethod
    def clear_all(cls):
        query = "DELETE FROM friendships"
        return connectToMySQL('friendships').query_db(query)

    @classmethod
    def check_for_friendship(cls, data): #False if empty, True if not
        query = "SELECT * FROM friendships WHERE (user_id = %(user_id)s AND friend_id = %(friend_id)s) OR (user_id = %(friend_id)s AND friend_id = %(user_id)s);"
        results = connectToMySQL('friendships').query_db(query, data)
        print("PRINTING CHECK FOR FRIENDSHIP")
        print(results)
        if results == ():
            return False
        else:
            return True