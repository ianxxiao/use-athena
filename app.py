from flask import Flask, render_template, request, g
from configs import db_config
from helper.db import get_db, insert_to_user_query
from helper.send_email import send_email
from helper.analytics import score_ideas

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
        name = request.form["name"]
        idea_1 = request.form["idea_1"]
        idea_2 = request.form["idea_2"]
        idea_3 = request.form["idea_3"]
        try:
            # insert_to_user_query(conn, email, [idea_1, idea_2, idea_3])
            ranked_ideas = score_ideas([idea_1, idea_2, idea_3])
            send_email(email, name, ranked_ideas)
            return render_template("success.html")
        except:
             return render_template("index.html", text="Hmm. Something went wrong. We are fixing it. Try again later?")


@app.teardown_appcontext
def close_connection(exception):
    cur = getattr(g, '_database', None)
    if cur is not None:
        print("Closing DB connection ...")
        cur.close()


if __name__ == '__main__':
    app.debug = True

    # TODO: Enable Postgres DB
    #create_db()

    app.run()
