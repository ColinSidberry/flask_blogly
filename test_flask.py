from unittest import TestCase

from app import app
from models import db, User, Post


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
        User.query.delete()
        Post.query.delete()
        # Question: can you programatically create a tables from the flask_test.py file
        # Note: create a function that calls the seed file
        user = User(first_name="Lizzy", last_name="Ahler")
        post = Post(title="Treats", content="Yummy pb treats", user_id=user.id)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()

        self.user_id = user.id
        self.post_id = post.id

    def tearDown(self):
        db.session.rollback()

    def test_home_route(self):
        with app.test_client() as client:
            resp = client.get('/', follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Lizzy', html)

    def test_user_list_page(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Lizzy', html)

    def test_render_new_user_page(self):
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button type="submit">Add</button>', html)

    def test_add_new_user(self):
        with app.test_client() as client:
            resp = client.post('/users/new', 
                data={'first_name': 'Colin', 
                        'last_name': 'Sidberry',
                        'img_url': ''}, follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Colin', html)
        #Question: how do we use the session variable to test if data made it to the db

    def test_show_post_page(self):
        with app.test_client() as client:
            breakpoint()
            resp = client.get('/posts/6')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Treats', html)


    