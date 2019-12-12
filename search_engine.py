# this is the main function of Athena
import urllib3
import sqlite3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import warnings
import re
import configs.search_engine_config as config

warnings.filterwarnings("ignore")


class Crawler:

    # Initialize the crawler with the name of database
    def __init__(self, dbname):

        try:
            self.conn = sqlite3.connect(dbname)
        except:
            print(">>>>> Cannot Connect to SQL DB. Terminate. <<<<<")

    def __del__(self):
        self.conn.close()

    def db_commit(self):
        self.conn.commit()

    def create_index_tables(self):
        # create tables
        self.conn.execute('create table URL_LIST(url)')
        self.conn.execute('create table WORD_LIST(word)')
        self.conn.execute('create table WORD_LOCATION(url_id, word_id, location)')
        self.conn.execute('create table LINK(from_id integer, to_id integer)')
        self.conn.execute('create table LINK_WORDS(word_id, link_id)')

        # index the tables
        self.conn.execute('create index word_idx on WORD_LIST(word)')
        self.conn.execute('create index url_idx on URL_LIST(url)')
        self.conn.execute('create index word_url_idx on WORD_LIST(word)')
        self.conn.execute('create index url_to_idx on LINK(to_id)')
        self.conn.execute('create index url_from_idx on LINK(from_id)')
        self.db_commit()

    # start with a list of pages, do a breadth first search to the given depth, index page as we go
    def crawl(self, pages, depth=2):

        http = urllib3.PoolManager()

        for i in range(depth):

            new_pages = set()
            for page in pages:
                try:
                    r = http.request('GET', page)
                except:
                    print("Could not get %s" % page)
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
                        url = url.split("#")[0]
                        if url[0:4] == 'http' and not self.is_indexed(url):
                            new_pages.add(url)
                        linkTest = self.get_text_only(link)
                        print(linkTest)
                        self.add_link_ref(page, url, linkTest)

                self.db_commit()
            pages = new_pages

        return len(links)

    # Auxilliary function for getting an entry id (add if it doesn't exist)
    def get_entry_id(self, table, field, value, create_new=True):
        cur = self.conn.execute("select rowid %s where %s = '%s'" % (table, field, value))
        res = cur.fetchone()
        if res is None:
            cur = self.conn.execute("insert into %s (%s) values ('%s')" % (table, field, value))
            return cur.lastrowid
        else:
            return res[0]

    # Index an individual page
    def add_to_index(self, url, soup):

        if self.is_indexed(url):
            return

        print('Indexing ' + url)

        # Get individual words
        text = self.get_text_only(soup)
        words = self.seperate_words(text)

        # Get the URL ID
        url_id = self.get_entry_id('URL_LIST', 'url', url)

        # Link each word to this URL
        for i in range(len(words)):
            word = words[i]
            if word in config.WORDS_IGNORE: continue
            word_id = self.get_entry_id('word_list', 'word', word)
            self.conn.execute("insert into WORD_LOCATION(url_id, word_id, location) values (%d, %d, %d)"
                              % (url_id, word_id, i))

    # Extract the text from an HTML page (no tags)
    def get_text_only(self, soup):
        v = soup.string
        if v is None:
            c = soup.contents
            result_text = ''
            for t in c:
                subtext = self.get_text_only(t)
                result_text += subtext + '\n'
            return result_text
        else:
            return v.strip()

    # Seperate the words by any non-whitespace character
    def seperate_words(self, text):
        splitter = re.complie('\\W*')
        return [s.lower() for s in splitter.split(text) if s != '']

    # Return true if this url is already indexed
    def is_indexed(self, url):
        u = self.conn.execute("select rowid from URL_LIST").fechone()
        if u is not None:
            # check if it actually has been crawled
            v = self.conn.execute("select * from WORD_LOCATION where url_id = %d" % u[0]).fetchone()
            if v is not None:
                return True
        return False

    # add a link between two pages
    def add_link_ref(self, url_From, url_To, link_Text):
        pass
