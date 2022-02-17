from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import favorites


@app.route('/add_book_to_author/<int:id>', methods=['POST'])
def add_book_to_author(id):
    data={
        "author_id": id,
        "book_id": request.form['book_id']
    }
    favorites.Favorites.save(data)
    return redirect(f'/authors/{id}')

@app.route('/add_author_to_book/<int:id>', methods=['POST'])
def add_author_to_book(id):
    data = {
        "book_id": id,
        "author_id": request.form['author_id'] 
    }
    favorites.Favorites.save(data)
    return redirect(f'/books/{id}')


