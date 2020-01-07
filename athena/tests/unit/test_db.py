import sys
sys.path.append('../use-athena')
import pytest
from athena.configs import db_config
from athena.helper import db_tmp, clean_db


@pytest.mark.parametrize("email, ideas, db_name", [("ian.xxiao@gmail.com",
                                                    ["my 1st idea", "my 2nd idea", "my 3rd idea"],
                                                    db_config.UNIT_TEST_DB_NAME)])
def test_db_user_query(email, ideas, db_name):

    # start a db
    conn = db_tmp.get_db(db_name)

    # run tests
    db_tmp.insert_to_user_query(conn, email, ideas)
    num_ideas = conn.execute("select DISTINCT(query) from USER_QUERY").fetchall()
    assert len(num_ideas) == len(ideas)

    # tear down the db
    clean_db.clean_test_db(db_name)
