"""Flask Application for Suyog's online resume."""
from flask import Flask, render_template
from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/main_page_tree")
def main_page_tree():
    return render_template("main_page_tree.html")


@app.route("/intro")
def intro():
    con = sqlite3.connect("flask.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(
        "select * from users where first_name = 'suyog' and last_name = 'somavanshi'"
    )

    rows = cur.fetchall()
    return render_template("intro.html", rows=rows)


@app.route("/education")
def education():
    con = sqlite3.connect("flask.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from education where user_first_name = 'suyog'")

    rows = cur.fetchall()
    return render_template("education.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
