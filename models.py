"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

Default_Image="https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()

### models go below !

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    "CupcateModel"
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text,nullable=False)
    size = db.Column(db.Text,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    image = db.Column(db.Text,nullable=False,default= Default_Image)

