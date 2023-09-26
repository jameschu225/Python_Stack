from flask_app.model import recipes
from flask_app.model import user
from flask import render_template, redirect, request, session, flash
from flask_app import app


@app.route("/recipes/create", methods=['post'])
def create_recipe():
    print(request.form)
    if not recipes.Recipe.recipe_validation(request.form):
        return redirect('/recipes/new')

    data = {
        "name" : request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
        "user_id":session["login_id"]
    }

    recipes.Recipe.creat_recipe(data)
    return redirect('/recipes')

@app.route("/recipes/<int:receipt_id>")
def show_one_receipt(receipt_id):
    receipt = recipes.Recipe.get_recipes_by_id(receipt_id)

    creator = user.User.get_user_by_id(receipt[0]["user_id"])
    return render_template("one_receipt.html", receipt=receipt[0], creator=creator, user= user.User.get_user_by_id(session["login_id"]))

@app.route("/recipes/edit/<int:receipt_id>")
def edit_one_receipt(receipt_id):
    if "login_id" not in session:
        return redirect('/')
    
    receipt = recipes.Recipe.get_recipes_by_id(receipt_id)
    print(receipt)
    # session["name"] = receipt[0]["name"]
    # session["description"] = receipt[0]["description"]
    # session["instructions"] = receipt[0]["instructions"]

    return render_template("update_receipt.html", receipt=receipt[0] )

@app.route("/recipes/update", methods=['post'])
def update_one_receipt():
    if not recipes.Recipe.recipe_validation(request.form):
        return redirect(f'/recipes/edit/{request.form["id"]}')

    recipes.Recipe.update(request.form)

    return redirect('/recipes')

@app.route("/recipes/delete/<int:receipt_id>")
def delete_one_receipt(receipt_id):
    
    recipes.Recipe.delete(receipt_id)

    return redirect('/recipes')

