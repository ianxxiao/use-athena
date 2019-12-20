from flask import Flask, render_template, request, g
from configs import db_config
import sqlite3
from helper.db import create_db, get_db, insert_to_user_query
from send_email import send_email

DATABASE = db_config.TEST_DB_NAME

app = Flask(__name__)


@app.route("/")
def index():
    conn = get_db(DATABASE)
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():

    # connect to the database
    conn = get_db(DATABASE)

    # collect the user inputs & insert to DB
    if request.method == 'POST':
        email = request.form["email_name"]
        idea_1 = request.form["idea_1"]
        idea_2 = request.form["idea_2"]
        idea_3 = request.form["idea_3"]
        try:
            insert_to_user_query(conn, email, [idea_1, idea_2, idea_3])
            send_email(email)
            return render_template("success.html")
        except:
             return render_template("index.html", text="Something went wrong. We are fixing it. Try again later?")


@app.teardown_appcontext
def close_connection(exception):
    cur = getattr(g, '_database', None)
    if cur is not None:
        print("Closing DB connection ...")
        cur.close()


if __name__ == '__main__':
    app.debug = True
    #create_db()
    app.run()
