# ---- Imports


import os
from flask import (
    Flask, flash, render_template, g, redirect, request, session, url_for)
from functools import wraps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# ---- Flask App Configuration


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ---- Credits:
# https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/get_pizzas")
def get_pizzas():
    pizzas = list(mongo.db.pizzas.find())
    return render_template("pizzas.html", pizzas=pizzas)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # ---- Checks if the username is already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # ---- Puts the new user into 'session'
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" not in session:
        if request.method == "POST":
            # ---- Check if user exists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ---- Makes sure hashed passwords match
                if check_password_hash(
                    existing_user['password'], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    flash(
                        "Welcome back {} ! Lets start making recipes!".format(
                            request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
                else:
                    # ---- Password doesnt match
                    flash(
                        "Incorrect Username and/or Password, try again please")
                    return redirect(url_for("login"))

            else:
                # ---- Username doesnt exist
                flash("Incorrect Username and/or Password, try again please")
                return redirect(url_for("login"))

        return render_template("login.html")

    # ---- If user is already logged in, redirect to profile page
    return redirect(url_for("profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        # ---- Checks if email already exists in db
        existing_email = mongo.db.subscribers.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("You are already subscribed to the Newsletter!")
            return redirect(url_for('get_pizzas'))
        # ---- Adds mail to subscribers collection in db
        subscribe = {
            "email": request.form.get("email").lower()
        }
        mongo.db.subscribers.insert_one(subscribe)

    flash("You are succesfully subscribed!")
    return redirect(url_for("get_pizzas"))


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        pizza = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "baking_time": request.form.get("baking_time"),
            "alergens": request.form.get("alergens"),
            "is_vegan": is_vegan,
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }

        mongo.db.pizzas.insert_one(pizza)
        flash("Recipe Successfully Added!")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<pizza_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(pizza_id):
    # ---- Only users can edit recipes
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    # ---- Edit recipe to db
    if request.method == "POST":
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        edited = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "baking_time": request.form.get("baking_time"),
            "alergens": request.form.get("alergens"),
            "is_vegan": is_vegan,
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.pizzas.update({"_id": ObjectId(pizza_id)}, edited)
        flash("Recipe is successfully edited")
        return redirect(url_for("profile", username=session['user']))

    pizza = mongo.db.pizzas.find_one({"_id": ObjectId(pizza_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", pizza=pizza, categories=categories)


@app.route("/delete_recipe/<pizza_id>")
@login_required
def delete_recipe(pizza_id):
    mongo.db.pizzas.remove({"_id": ObjectId(pizza_id)})
    flash("Recipe is succesfully deleted")
    return redirect(url_for("profile", username=session['user']))


@app.route("/categories")
@login_required
def categories():
    if not session.get("user") == "admin":
        return render_template("error_handlers/404.html")

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(category)
        flash("New category is succesfully added")
        return redirect(url_for("categories"))

    return render_template("add_category.html")



# ---- Error Handlers


@app.errorhandler(404)
def not_found(e):
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error_handlers/500.html"), 500


@app.errorhandler(403)
def forbidden(e):
    return render_template("error_handlers/403.html"), 403


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # ---- Dont forget to change debug = False
