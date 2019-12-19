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

    return conn.cursor()


def create_index_tables(conn):
    # create tables
    conn.execute('create table URL_LIST(url)')
    conn.execute('create table WORD_LIST(word)')
    conn.execute('create table WORD_LOCATION(url_id, word_id, location)')
    conn.execute('create table LINK(from_id integer, to_id integer)')
    conn.execute('create table LINK_WORDS(word_id, link_id)')
    conn.execute('create table USER_QUERY(email, query)')

    # index the tables
    conn.execute('create index word_idx on WORD_LIST(word)')
    conn.execute('create index url_idx on URL_LIST(url)')
    conn.execute('create index word_url_idx on WORD_LIST(word)')
    conn.execute('create index url_to_idx on LINK(to_id)')
    conn.execute('create index url_from_idx on LINK(from_id)')
    conn.execute('create index email_idx on USER_QUERY(email)')
    conn.commit()


def insert_to_db(conn, table, field, values):
    for value in values:
        conn.execute("insert into %s (%s) values ('%s')" % (table, field, value))
