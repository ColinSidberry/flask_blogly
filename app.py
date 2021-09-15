"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
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
def show_users():
    return redirect('/users')

@app.get('/users')
def get_users():
    title = "Users"
    users = User.query.all()
    return render_template('index.html', 
        title = title,
        users = users)

@app.get('/users/new')
def show_form():
    title = "Create a user"
    return render_template('create_user.html',
        title = title)

@app.post('/users/new')
def add_user():
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form.get('img_url')
    breakpoint()
    new_user = User(
        first_name=first_name, 
        last_name=last_name, 
        img_url=img_url)

    db.session.add(new_user)
    db.session.commit()
    print("got past new user commit")
    #flash('New users successfully added!')
    
    return redirect('/users')



