import sys
sys.path.append('../use-athena')
import psycopg2
from athena.configs import db_config
import time

def create_table():
    conn = psycopg2.connect(dbname=db_config.DB_NAME,
                            user=db_config.DB_USER,
                            password=db_config.DB_PW,
                            host=db_config.HOST,
                            port=db_config.PORT)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS USER_QUERY (email TEXT, query TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

def insert_to_user_query(email, query_values):
    """
    This function writes to the database
    Inputs:
        idx: the index field (e.g. email)
        values: a list of values to be inserted in (e.g. [idea_1, idea_2, idea_3])
    """
    conn = psycopg2.connect(dbname=db_config.DB_NAME,
                            user=db_config.DB_USER,
                            password=db_config.DB_PW,
                            host=db_config.HOST,
                            port=db_config.PORT)
    cur = conn.cursor()

    timestamp = str(time.strftime('%Y%m%d%H%M%S'))

    for query in query_values:
        cur.execute("insert into USER_QUERY(email, query, timestamp) "
                  "values ('%s', '%s', '%s')" % (email, query, timestamp))

    conn.commit()
    conn.close()