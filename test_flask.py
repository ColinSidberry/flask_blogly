from unittest import TestCase

from app import app
from models import db, User


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Test for views for Users."""

    def setUp(self):
        # Question: can you programatically create a tables from the flask_test.py file
        user = User(first_name="Lizzy", last_name="Ahler")
        db.session.add(user)
        db.session.commit()

        self.use_id = user.id

    def tearDown(self):
        db.session.rollback()
        # ToDo/Question: what does this do again?

    def test_home_route(self):
        with app.test_client() as client:
            resp = client.get('/')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/users')

    def test_user_list_page(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/users/new">' ,html)
