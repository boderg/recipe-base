# The Code Institute tutorial for task manager
# was used as a reference to build this project.
# This code has been adapted and added to in order
# to create the Recipe Base website.

# Imports
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from datetime import datetime
if os.path.exists("env.py"):
    import env


# Flask app
app = Flask(__name__, template_folder="templates")


# Configuration for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Route for the home page
@app.route("/")
def home():
    return render_template("home.html")


# Route for the recipes page
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Route for the search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Route for the register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if passwords match
        if request.form.get("password") != request.form.get("password2"):
            flash("Passwords do not match")
            return redirect(url_for("register"))

        # create a new user
        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email"),
            "bio": request.form.get("bio"),
            "join_date": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get(
                    "username").capitalize()))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Route to logout
@app.route("/logout")
def logout():

    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Route to view the user's profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session.get("user"):

        # grab the session user's username from db
        if session["user"] == username:
            user = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "profile.html", username=username, user=user)

        # if the user is not the session user
        else:
            flash("You can only view your own profile")
            return redirect(url_for("profile", username=session['user']))

    # if there is no session user
    else:
        flash("Please login to view your profile")
        return render_template("login.html")


# Route to edit the user's profile
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if not session.get("user"):
        flash("Please login to edit your profile")
        return redirect(url_for("login"))

    if request.method == "POST":
        edit = {
                "email": request.form.get("email"),
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "bio": request.form.get("bio"),
                "profile_image": request.form.get("profile_image"),
                "updated_on": datetime.now().strftime("%d-%m-%Y at %H:%M")
            }
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$set": edit}
        )
        flash("Profile Successfully Updated")
        return redirect(url_for("profile", username=session['user']))

    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("edit_profile.html", username=username, user=user)


# Route to delete the user's profile
@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.delete_one({"username": session["user"]})
    flash("User Successfully Deleted")
    session.pop("user")
    return redirect(url_for("login"))


# Route to add a recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not session.get("user"):
        flash("Please login to add a recipe")
        return redirect(url_for("login"))

    if request.method == "POST":
        recipe = {
            "category_name": request.form.getlist("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "optional_ingredients": request.form.getlist(
                "optional_ingredients"),
            "preparation_time": request.form.get("preparation_time"),
            "preparation_method": request.form.getlist("preparation_method"),
            "cooking_time": request.form.get("cooking_time"),
            "cooking_method": request.form.getlist("cooking_method"),
            "serving_size": request.form.get("serving_size"),
            "created_by": session["user"],
            "recipe_image": request.form.get("recipe_image"),
            "created_on": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Route to edit a recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not session.get("user"):
        flash("Please login to edit the recipe")
        return redirect(url_for("login"))

    if request.method == "POST":
        edit = {
            "category_name": request.form.getlist("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "optional_ingredients": request.form.getlist(
                "optional_ingredients"),
            "preparation_time": request.form.get("preparation_time"),
            "preparation_method": request.form.getlist("preparation_method"),
            "cooking_time": request.form.get("cooking_time"),
            "cooking_method": request.form.getlist("cooking_method"),
            "serving_size": request.form.get("serving_size"),
            "created_by": session["user"],
            "recipe_image": request.form.get("recipe_image"),
            "created_on": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": edit})
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipe", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Route to delete a recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# Route to view a single recipe
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # if there is a session user
    if session.get("user"):
        return render_template("recipe.html", recipe=recipe)

    # if there is no session user
    else:
        flash("Please login to view the recipe")
        return render_template("recipes.html", recipe=recipe)


# Route to view the categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    # if there is a session user
    if session.get("user"):
        return render_template("categories.html", categories=categories)

    # if there is no session user
    else:
        flash("Please login to view the categories")
        return render_template("login.html", categories=categories)


# Route to add a category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if not session.get("user"):
        flash("Please login to add a category")
        return redirect(url_for("login"))

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Route to edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if not session.get("user"):
        return redirect(url_for("login"))

    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image"),
            "updated_on": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.categories.replace_one({"_id": ObjectId(category_id)}, edit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Route to delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Route to view a single category
@app.route("/single_category/<category_id>")
def single_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    recipes = list(mongo.db.recipes.find(
        {"category_name": category["category_name"]}))

    # if there is a session user
    if session.get("user"):
        return render_template(
            "single_category.html", category=category, recipes=recipes)

    # if there is no session user
    else:
        flash("Please login to view this recipe")
        return render_template(
            "login.html", category=category, recipes=recipes)


# Route if the page is not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# Route if there is an internal server error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


# Main function to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
