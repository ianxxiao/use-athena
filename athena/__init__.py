from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from athena.helper.db import create_table
import os


# setup env vars
if os.path.exists(".env"):
    print("found environment var, setting up ...")
    from dotenv import load_dotenv

    load_dotenv()

# start up the flask app
flask_app = Flask(__name__)

# set up the db tables
# TODO: PARAMETERIZE THE KEY
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
db = SQLAlchemy(flask_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

flask_app.config['SECRET_KEY'] = '03b6642efc7533bf2aba6c155045ce3c'
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = ''
# db = SQLAlchemy

from athena import user_landing_route



