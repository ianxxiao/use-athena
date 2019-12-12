# this is the main funcation of Athena
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin

WORDS_IGNORE = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler:

    # Initialize the crawler with the name of database
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def db_commit(self):
        pass

    # Auxilliary function for getting an entry id (add if it doesn't exist)
    def get_entry_id(self, table, field, value, create_new=True):
        return None

    # Index an individual page
    def add_to_index(self, url, soup):
        print("Indexing %s" % url)

    # Extract the text from an HTML page (no tags)
    def get_text_only(self, soup):
        return None

    # Seperate the words by any non-whitespace character
    def seperate_words(self, text):
        return None

    # Return true if this url is alread indexed
    def is_indexed(self, url):
        return False

    # add a link between two pages
    def add_link_ref(self, url_From, url_To, link_Text):
        pass

    # start with a list of pages, do a breadth first search to the given depth, index page as we go
    def crawl(self, pages, depth=2):

        http = urllib3.PoolManager()

        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    r = http.request('GET', page)
                except:
                    print("Could not open %s" % page)
                    continue

                # parse content with BeautifulSoup
                soup = BeautifulSoup(r.data)
                self.add_to_index(page, soup)

                # get all the links in the page
                links = soup('a')

                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1: continue
                    url=url.split("#")[0]
                    if url[0:4] == 'http' and not self.is_indexed(url)
                        newpages.add(url)
                    linkTest = self.get_text_only(link)
                    self.add_link_ref(page, url, linkTest)

                self.db_commit()

            pages = newpages

    # create the database tables
    def create_index_tables(self):
        pass


def cal_addition(a, b):
    return int(a) + int(b)


if __name__ == '__main__':
    print(">>>>> " + str(cal_addition(2, 4)))
