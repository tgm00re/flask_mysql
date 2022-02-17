from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models import book

@app.route('/')
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

@app.route('/create_author', methods=['POST'])
def create_author():
    author_data = {
        "name": request.form['name']
    }
    Author.save(author_data)
    return redirect('/')


@app.route('/authors/<int:id>')
def single_author(id):
    data = {
        "id": id
    }
    author_with_books = Author.get_author_with_books(data)
    books = book.Book.get_all()
    print(author_with_books)
    return render_template("display_author.html", author_with_books=author_with_books, books=books, id=id)
