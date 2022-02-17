from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, book


class Favorites:
    def __init__(self, data):
        self.book_id = data['book_id']
        self.author_id = data['author_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s)"
        return connectToMySQL('books').query_db(query, data)