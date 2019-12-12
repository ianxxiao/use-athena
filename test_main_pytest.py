import pytest

@pytest.mark.parametrize("pagelist, num_links", [(['https://en.wikipedia.org/wiki/Star_Wars'], 10)])
def test_crawler(pagelist, num_links):
    # test if the crawler can get at least 10 links from the Star War Wiki Page
    from search_engine import crawler
    crawler = crawler('')

    assert crawler.crawl(pagelist) >= num_links
