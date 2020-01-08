from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# db = SQLAlchemy

from athena import routes
