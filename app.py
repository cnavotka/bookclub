import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home
@app.route("/")
@app.route("/home")
def home():
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "home.html", user=user)
    else:
        return render_template("home.html")


# Sign up
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        # check if the username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Hi, {}. Welcome to books'world.".format(
                        request.form.get("username").capitalize()))
        flash("Click on the add button and create your fisrt book summary")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("sign_up.html")


# Log in page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid passwword match
                flash("Incorrect Username and/or Password")
                return render_template("login.html")

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return render_template("login.html")

    return render_template("login.html")


# Profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # get the session user's books from database
    books = list(mongo.db.books.find())

    # get random quote from database
    quotes = mongo.db.quotes.aggregate([{"$sample": {"size": 1}}])

    if session["user"]:
        return render_template(
            "profile.html", username=username, books=books, quotes=quotes)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("home"))


# Add a new into database
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_name": request.form.get("book_name"),
            "book_writer": request.form.get("book_writer"),
            "img_url": request.form.get("img_url"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        return redirect("/profile/<username>")


# View Book page
@app.route("/view_book/<book_name>")
def view_book(book_name):
    book = mongo.db.books.find_one({"_id": ObjectId(book_name)})
    return render_template("view_book.html", book=book)


# Edit book route
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        edited_book = {
            "book_name": request.form.get("book_name"),
            "book_writer": request.form.get("book_writer"),
            "img_url": request.form.get("img_url"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, edited_book)

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("view_book.html", book=book)


# Delete Book
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    return redirect("/profile/<username>")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
