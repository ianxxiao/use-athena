# this script remove all test DBs from folder to release storage

import os
import configs.search_engine_config as config


def clean_test_db():
    if os.path.isfile(config.TEST_DB_NAME):
        print("clean up test db ...")
        os.remove(config.TEST_DB_NAME)
    else:
        pass


def clean_dev_db():
    if os.path.isfile(config.DEV_DB_NAME):
        os.remove(config.DEV_DB_NAME)
    else:
        pass
