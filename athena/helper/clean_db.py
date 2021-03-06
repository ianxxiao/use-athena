# this script remove all test DBs from folder to release storage

import os
import athena.configs.db_config as config


def clean_test_db(db_name):
    if os.path.isfile(db_name):
        print("clean up test db ...")
        os.remove(db_name)
    else:
        pass


def clean_dev_db():
    if os.path.isfile(config.DEV_DB_NAME):
        os.remove(config.DEV_DB_NAME)
    else:
        pass
