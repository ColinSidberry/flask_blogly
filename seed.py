"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add User
colin = User(first_name='Colin', last_name='Sidberry')
lizzy = User(first_name='Lizzy', last_name='Ahler')

# Add new objects to session, so they'll persist
db.session.add(colin)
db.session.add(lizzy)

# Commit--otherwise, this never gets saved!
db.session.commit()

# 1. create db = users
# 2. seed the db with our seed file
# 3. run server
# 4. test routes