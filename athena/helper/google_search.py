import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_title(url):
    """
    This function returns the title of based on HTML of a url.
    Inputs:
        url (str): a url string
    Outputs:
        title (str): the title based on HTML tag
    """

    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')

    return soup.title.string


def google_search(query_list, n=5):
    """
    This function performs a google search and returns the top n results.
    Inputs:
        query (tuple): a list of the search term and score tuple (e.g. [term, score])
        n (int): the number of results
    Output:
        search_results (dict): a dictionary of top n results (key: search_term, value: a list of url and titles)
    """

    title_url = []
    search_results = {}

    for query in query_list:

        for url in search(query[0] + " Medium.com", tld="com", pause=0.8, start=2, stop=n):
            title_url.append([str(url), get_title(url)])

        search_results[query[0]] = title_url
        title_url = []

    return search_results
