import pytest

from configs import search_engine_config
import os.path


@pytest.mark.parametrize("page_list, db_name, num_links", [(['https://en.wikipedia.org/wiki/Star_Wars'],
                                                           search_engine_config.TEST_DB_NAME, 3000)])
def test_crawler(page_list, db_name, num_links):
    from search_engine import Crawler
    crawler = Crawler(db_name)

    # test if db set up works properly
    assert os.path.isfile(db_name)
    # test if the crawler can get at least 3000 links from the Star War Wiki Page
    assert crawler.crawl(page_list, depth=1) >= num_links
