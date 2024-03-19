import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        # check if passwords match
        if request.form.get("password") != request.form.get("password2"):
            flash("Passwords do not match")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


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
                flash("Welcome, {}".format(request.form.get("username").capitalize()))
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


@app.after_request
def add_no_cache_headers(response):
    if 'Cache-Control' not in response.headers:
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "-1"
    return response


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session.get("user"):
        if session["user"] == username:
            user = mongo.db.users.find_one({"username": session["user"]})
            return render_template("profile.html", username=username, user=user)
        else:
            flash("You can only view your own profile")
            return redirect(url_for("profile", username=session['user']))
    else:
        flash("Please login to view your profile")
        return render_template("login.html")


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
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


@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.delete_one({"username": session["user"]})
    flash("User Successfully Deleted")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.getlist("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "optional_ingredients": request.form.getlist("optional_ingredients"),
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


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "category_name": request.form.getlist("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "optional_ingredients": request.form.getlist("optional_ingredients"),
            "preparation_time": request.form.get("preparation_time"),
            "preparation_method": request.form.getlist("preparation_method"),
            "cooking_time": request.form.get("cooking_time"),
            "cooking_method": request.form.getlist("cooking_method"),
            "serving_size": request.form.get("serving_size"),
            "created_by": session["user"],
            "recipe_image": request.form.get("recipe_image"),
            "created_on": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": edit})
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if session.get("user"):
        return render_template("single_recipe.html", recipe=recipe)
    else:
        flash("Please login to view the recipe")
        return render_template("recipes.html", recipe=recipe)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    if session.get("user"):
        return render_template("categories.html", categories=categories)
    else:
        flash("Please login to view the categories")
        return render_template("login.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.replace_one({"_id": ObjectId(category_id)}, edit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/single_category/<category_id>")
def single_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    recipes = list(mongo.db.recipes.find({"category_name": category["category_name"]}))
    if session.get("user"):
        return render_template("single_category.html", category=category, recipes=recipes)
    else:
        return render_template("login.html", category=category, recipes=recipes)
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
