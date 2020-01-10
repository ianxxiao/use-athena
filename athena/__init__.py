from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from athena.helper.db import create_table
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


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
login_manager = LoginManager(flask_app)


from athena import user_landing_route



