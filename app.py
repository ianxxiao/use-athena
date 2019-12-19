from flask import Flask, render_template, request, g
from configs import search_engine_config
import sqlite3
from helper.db import get_db

DATABASE = search_engine_config.TEST_DB_NAME

app = Flask(__name__)


@app.route("/")
def index():
    cur = get_db(DATABASE)
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        idea_1 = request.form["idea_1"]
        idea_2 = request.form["idea_2"]
        idea_3 = request.form["idea_3"]
        print(email)
        print(idea_1, idea_2, idea_3)
    return render_template("success.html")


@app.teardown_appcontext
def close_connection(exception):
    cur = getattr(g, '_database', None)
    if cur is not None:
        cur.close()


if __name__ == '__main__':
    app.debug = True
    app.run()
