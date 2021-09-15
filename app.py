"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretkey"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.get('/')
def get_users():
    title = "Users"
    users = User.query.all()
    return render_template('index.html', 
        title = title,
        users = users)


