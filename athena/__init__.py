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
create_table()

# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# db = SQLAlchemy

from athena import routes



