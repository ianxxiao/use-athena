# this script remove all test DBs from folder to release storage

import os
import configs.search_engine_config as config


def clean_test_db():
    os.remove(config.TEST_DB_NAME)


def clean_dev_db():
    os.remove(config.DEV_DB_NAME)
