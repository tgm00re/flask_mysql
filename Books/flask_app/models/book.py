from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, db_data):
        self.id = db_data['id'],
        self.title = db_data['title'],
        self.num_of_pages = db_data['num_of_pages'],
        self.created_at = db_data['created_at'],
        self.updated_at = db_data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books').query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        book = cls( results[0] )

        for row_from_db in results:
            author_data = {
                "id": row_from_db['authors.id'],
                "name": row_from_db['name'],
                "created_at": row_from_db['created_at'],
                "updated_at": row_from_db['updated_at']
            }
            book.authors.append( author.Author(author_data) )
        return book
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES(%(title)s, %(num_of_pages)s, NOW(), NOW() )"
        return connectToMySQL('books').query_db(query, data)
    