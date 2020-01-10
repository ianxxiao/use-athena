from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from athena.helper.db import create_table
import os
from datetime import datetime
from flask_bcrypt import Bcrypt


# setup env vars
if os.path.exists(".env"):
    print("found environment var, setting up ...")
    from dotenv import load_dotenv

    load_dotenv()

# start up the flask app
flask_app = Flask(__name__)

# Configuration
# TODO: PARAMETERIZE THE KEY
flask_app.config['SECRET_KEY'] = '03b6642efc7533bf2aba6c155045ce3c'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
db = SQLAlchemy(flask_app)
bcrypt = Bcrypt(flask_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


from athena import user_landing_route



