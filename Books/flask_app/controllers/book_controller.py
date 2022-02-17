from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.controllers.author_controller import authors
from flask_app.models.book import Book
from flask_app.models import author


@app.route('/books')
def books():
    books = Book.get_all()
    return render_template("books.html", books=books)

@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    Book.save(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def single_book(id):
    data = {
        "id": id
    }
    book_with_authors = Book.get_book_with_authors(data)
    authors = author.Author.get_all()
    return render_template("display_book.html", book_with_authors=book_with_authors, authors=authors, id=id)