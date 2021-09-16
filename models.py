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
    #ToDo - check for valid img URL
    #Question - when given a default, should we be explicit and set nullable to false
    # Question 2: How default img to be triggered. Entering no img url from the frontend currently doesn't pull the default img

    # Taken from morning demo
    # def greet(self):
    #     """Greet using name."""

    #     return f"I'm {self.name} the {self.species or 'thing'}"

    # def feed(self, units=10):
    #     """Nom nom nom."""

    #     self.hunger -= units
    #     self.hunger = max(self.hunger, 0)

    # def __repr__(self):
    #     """Show info about pet."""

    #     p = self
    #     return f"<Pet {p.id} {p.name} {p.species} {p.hunger}>"

    # @classmethod
    # def get_by_species(cls, species):
    #     """Get all pets matching that species."""

    #     return cls.query.filter_by(species=species).all()
