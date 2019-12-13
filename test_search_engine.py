import pytest
from configs import search_engine_config
from helper import clean_db
import sqlite3
import os
from search_engine import Crawler

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
