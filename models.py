"""Models for Blogly."""

"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False)
    last_name = db.Column(db.String(50),
                    nullable=False)
    img_url = db.Column(db.String(5000), nullable = False, default = DEFAULT_IMG_URL) 

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                    nullable=False)
    content = db.Column(db.Text(),
                    nullable=False)
    created_at = db.DateTime(timezone = True)
    user_id = db.Column(db.Integer,
                    db.ForeignKey('users.id'))
    user = db.relationship('User', backref='posts')
   