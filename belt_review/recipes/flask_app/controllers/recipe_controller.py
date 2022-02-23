import bcrypt
from flask import redirect, render_template, session, request, flash
from flask_app import app
from flask_app.models import recipe

@app.route('/add_recipe')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("add_recipe.html")

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/add_recipe')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "made_on": request.form['made_on'],
        "under_thirty": request.form['under_thirty'],
        "creator_id": session['user_id']
    }
    recipe.Recipe.save(data)
    return redirect('/dashboard')

@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    recipe_to_edit = recipe.Recipe.get_single(data)
    if recipe_to_edit.creator_id[0] != session['user_id']:
        return redirect('/dashboard')
    return render_template("edit_recipe.html", recipe_id=id)

@app.route('/update_recipe/<int:id>', methods=['POST'])
def update_recipe(id):
    if not recipe.Recipe.validate_recipe(request.form):
        print("RECIPE INVALID :(")
        return redirect('/edit_recipe')
    data = {
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "made_on": request.form['made_on'],
        "under_thirty": request.form['under_thirty']
    }
    print("EDITING RECIPE")
    recipe.Recipe.edit_one(data)
    return redirect('/dashboard')

@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    data = {
        "id": id
    }
    recipe.Recipe.delete_one(data)
    return redirect('/dashboard')

@app.route('/display_recipe/<int:id>')
def display_recipe(id):
    data = {
        "id": id
    }
    single_recipe = recipe.Recipe.get_single(data)
    return render_template("display_recipe.html", recipe=single_recipe)