from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    def __init__(self, db_data):
        self.id = db_data['id'],
        self.name = db_data['name'],
        self.created_at = db_data['created_at'],
        self.updated_at = db_data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    #SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;
    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        print("PRINTING RESULTS C:")
        print(results)

        author = cls( results[0] )

        for row_from_db in results:
            #Create instances of books and add them into our list
            book_data = {
                "id": row_from_db["books.id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            author.books.append( book.Book(book_data) )
        #Keep in mind you are only returning a SINGLE author with books! 
        return author

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() )"
        return connectToMySQL('books').query_db(query,data)

    
