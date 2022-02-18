from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, db_data):
        self.id = db_data['id'],
        self.first_name = db_data['first_name'],
        self.last_name = db_data['last_name'],
        self.created_at = db_data['created_at'],
        self.updated_at = db_data['updated_at']
        self.friends = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('friendships').query_db(query)
        users = []
        for single_user in results:
            users.append( cls(single_user) )
        return users

    @classmethod
    def get_possible_friends(cls, data):
        query = "SELECT * FROM users WHERE id <> %(id)s"
        results = connectToMySQL('friendships').query_db(query,data)
        users = []
        for single_user in results:
            users.append( cls(single_user))

    @classmethod
    def get_friendships(cls):
        query = "SELECT * FROM users JOIN friendships ON users.id = friendships.user_id JOIN users as user2 ON friendships.friend_id = user2.id;"
        results = connectToMySQL('friendships').query_db(query)
        print("PRINTING RESULTS")
        print(results)
        friendships = []

        for row_from_db in results:
            friend_data = {
                "user_first_name": row_from_db['first_name'],
                "user_last_name": row_from_db['last_name'],
                "friend_first_name": row_from_db['user2.first_name'],
                "friend_last_name": row_from_db['user2.last_name']
            }
            friendships.append(friend_data)
        return friendships
        


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        return connectToMySQL('friendships').query_db(query, data)

    