from googlesearch import search


def google_search(query_list, n=10):
    """
    This function performs a google search and returns the top n results.
    Inputs:
        query (list): a list of the search term
        n (int): the number of results
    Output:
        top_n_results (list): a list of top n results (link and title)
    """

    top_n_results = []
    search_results = []
    for query in query_list:
        for i in search(query[0] + " Medium.com", tld="com", pause=1.0, stop=n):
            top_n_results.append(i)
        search_results.append(top_n_results)
        top_n_results = []
    return search_results
