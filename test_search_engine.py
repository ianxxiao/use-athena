import pytest

@pytest.mark.parametrize("pagelist, num_links", [(['https://en.wikipedia.org/wiki/Star_Wars'], 3000)])
def test_crawler(pagelist, num_links):
    # test if the crawler can get at least 3000 links from the Star War Wiki Page
    from search_engine import crawler
    crawler = crawler('')

    assert crawler.crawl(pagelist, depth=1) >= num_links
