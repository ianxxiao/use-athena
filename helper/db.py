# This script includes all helper functions to manage SQLite DB
import sqlite3
import os


def get_db(DATABASE):
    # stand up a db if it does not exist
    if os.path.isfile(DATABASE) is False:
        try:
            conn = sqlite3.connect(DATABASE)
            create_index_tables(conn)
        except:
            print(">>>>> Cannot Create a new SQL DB. Terminate. <<<<<")
    else:
        try:
            conn = sqlite3.connect(DATABASE)
        except:
            print(">>>>> Something is Wrong. Cannot Connect to DB. <<<<<<")

    return conn


def create_index_tables(conn):
    # create tables
    c = conn.cursor()
    c.execute('create table URL_LIST(url)')
    c.execute('create table WORD_LIST(word)')
    c.execute('create table WORD_LOCATION(url_id, word_id, location)')
    c.execute('create table LINK(from_id integer, to_id integer)')
    c.execute('create table LINK_WORDS(word_id, link_id)')
    c.execute('create table USER_QUERY(email, query)')

    # index the tables
    c.execute('create index word_idx on WORD_LIST(word)')
    c.execute('create index url_idx on URL_LIST(url)')
    c.execute('create index word_url_idx on WORD_LIST(word)')
    c.execute('create index url_to_idx on LINK(to_id)')
    c.execute('create index url_from_idx on LINK(from_id)')
    c.execute('create index email_idx on USER_QUERY(email)')
    conn.commit()


def insert_to_user_query(conn, email, query_values):
    """
    This function writes to the database
    Inputs:
        conn: a class of the connection
        table: the table the values will be inserted to
        idx: the index field (e.g. email)
        values: a list of values to be inserted in (e.g. [idea_1, idea_2, idea_3])
    """
    c = conn.cursor()
    for query in query_values:
        try:
            conn.execute("insert into USER_QUERY(email, query) values ('%s', '%s')" % (email, query))
            print("done inserting")
        except:
            print("didn't work")
    conn.commit()