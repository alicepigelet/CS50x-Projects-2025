from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from helpers import lookup_emissions, generate_report
import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_query():
    query = request.form.get("query")
    results = lookup_emissions(query)
    print ("Query:", query)
    print("Results:", results)
    return render_template("results.html", data=results, query=query)

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    results = lookup_emissions(query)
    return render_template("results.html", data=results, query=query)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return  render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
