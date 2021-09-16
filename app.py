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
    """Redirects to /users, which shows a list of all the users"""
    return redirect('/users')

@app.get('/users')
def get_users():
    """Shows a list of all the users"""

    title = "Users" #Note: Do this all in the template
    users = User.query.all()
    return render_template('index.html', 
        title = title,
        users = users)

@app.get('/users/new')
def show_form():
    """Shows a form to submit a new user to the database"""

    title = "Create a user"
    return render_template('create_user.html',
        title = title)

@app.post('/users/new')
def add_user():
    """Submits a new user to the database and redirects to the main list of users"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] or None #Note: We are sending an empty string
    
    new_user = User(
        first_name=first_name, 
        last_name=last_name, 
        img_url=img_url)

    db.session.add(new_user)
    db.session.commit()
    
    flash('New users successfully added!')
    
    return redirect('/users')


@app.get('/users/<int:user_id>')
def show_user_details(user_id):
    """Takes in user ID from URL and shows page of that users details"""

    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html',
        user_id = user_id,
        title = f"{user.first_name} {user.last_name}", #Note - better to have this as an instance method in our model
        img_url = user.img_url)

@app.get('/users/<int:user_id>/edit')
def show_edit_user(user_id):
    """Takes in user ID from URL and shows an edit page for that user"""

    user = User.query.get(user_id)
    title = "Edit a user"

    return render_template("edit_user.html",
        user = user, 
        title = title)
       
        #Note: Pass the user object and let the template do the work


@app.post('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Takes in user ID from URL and updates database with edits to user instance. 
        Redirects to main list of users"""
    user = User.query.get_or_404(user_id)
        
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] #Note: SQL Alchemy won't set a default on update

    user.first_name = first_name
    user.last_name = last_name
    user.img_url = img_url
    
    db.session.commit()
    return redirect('/users')

@app.post('/users/<int:user_id>/delete')
def remove_user(user_id):
    """Takes in user ID from URL and removes user from database. Redirects to main list of users."""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')