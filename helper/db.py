# This script includes all helper functions to manage SQLite DB
# https://www.robinwieruch.de/postgres-sql-macos-setup
import sys
sys.path.append('../use-athena')
import sqlite3
import os
import time
import psycopg2
from configs import db_config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.types import String

def create_db():

    """
    This function starts a postgres db.
    Inputs:

    Return:
        None
    """
    print("setting up postgres database ...")
    user = "postgres"
    host = "127.0.0.1"
    port = "5432"
    database = "athena_dev"
    conn = psycopg2.connect(user=user,
                            host=host,
                            port=port,
                            database=database)

    # check if the database exists
    cur = conn.cursor()
    cur.execute(f"select datname from pg_catalog.pg_database where datname='{database}'")
    if cur.fetchone() is None:
        print("creating a new database ...")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute(f'create database {database}')
    else:
        print("database already exist ...")
    cur.close()
    conn.close()


def get_db(DATABASE):
    """
    This function connects to the database or create a new one if it does not exist.
    Inputs:
        DATABASE (str): the name of the database
    Return:
        conn: connection class
    """

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
    """
    This function initialize all the tables and index them
    input:
        conn: connection class
    output:
        None
    """

    # create tables
    c = conn.cursor()
    c.execute('create table URL_LIST(url)')
    c.execute('create table WORD_LIST(word)')
    c.execute('create table WORD_LOCATION(url_id, word_id, location)')
    c.execute('create table LINK(from_id integer, to_id integer)')
    c.execute('create table LINK_WORDS(word_id, link_id)')
    c.execute('create table USER_QUERY(email, query, timestamp)')

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
    timestamp = str(time.strftime('%Y%m%d%H%M%S'))
    for query in query_values:
        c.execute("insert into USER_QUERY(email, query, timestamp) "
                  "values ('%s', '%s', '%s')" % (email, query, timestamp))

    conn.commit()