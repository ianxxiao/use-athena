import sys
sys.path.append('../use-athena')
import pytest
from configs import search_engine_config
from helper import clean_db
import sqlite3
import os
from search_engine import Crawler
import mechanize


# @pytest.mark.parametrize("email, ideas, db_name", [("ian.xxiao@gmail.com",
#                                                     ["my 1st idea", "my 2nd idea", "my 3rd idea"],
#                                                     search_engine_config.TEST_DB_NAME)])
# def test_app_idea_entry(email, ideas, db_name):
#     # https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
#
#     # clean the db
#     clean_db.clean_test_db()
#
#     # start the app
#     os.system("python app.py")
#
#     # create a mechanize bot
#     br = mechanize.Browser()
#     br.set_handle_robots(False)  # ignore robots
#     br.set_handle_refresh(False)  # can sometimes hang without this
#     br.open("http://127.0.0.1:5000/")
#     br.select_form("user_ideas")
#     br.form['email_name'] = 'ian.xxiao@gmail.com'
#     br.form['idea_1'] = 'my idea 1'
#     br.form['idea_2'] = 'my idea 2'
#     br.form['idea_3'] = 'my idea 3'
#     br.submit()
#
#     # query database
#     conn = sqlite3.connect(db_name)
#     res = conn.execute("select url from URL_LIST").fetchall()
#     assert len(res) == len(ideas)

page_list = ['https://en.wikipedia.org/wiki/James_Bond', 'https://en.wikipedia.org/wiki/Star_Wars']

@pytest.mark.parametrize("pages, db_name", [(page_list, search_engine_config.TEST_DB_NAME)])
def test_crawler(pages, db_name):
    clean_db.clean_test_db()
    crawler = Crawler(db_name)
    crawler.crawl(pages, depth=1)
    conn = sqlite3.connect(db_name)

    # test if db set up works properly
    assert os.path.isfile(db_name)

    # test if all urls are indexed properly
    res = conn.execute("select url from URL_LIST").fetchall()
    assert len(res) == len(page_list)

    # test if word counts are sensible
    res = conn.execute("select count(*) from WORD_LIST").fetchall()
    assert res[0][0] >= 20000

    # test if URL-WORD is indexed properly
    res = conn.execute("select DISTINCT(url_id) from WORD_LOCATION").fetchall()
    assert len(res) == len(page_list)

    crawler.__del__()
