from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from athena.helper.db import create_table

flask_app = Flask(__name__)
create_table()
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# db = SQLAlchemy

from athena import routes



