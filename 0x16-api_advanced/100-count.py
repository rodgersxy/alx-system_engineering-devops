#!/usr/bin/python3

"""
a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should coun
t as javascript, but java should not).
"""

import requests


# Define a function called count_words that takes several parameters
def count_words(subreddit, word_list, dictWord={}, after=None):
    """
    Recursive function that queries the Reddit API
    """
    # Check if the 'subreddit' parameter is None
    if subreddit is None:
        print(None)

    # Define the URL to query the Reddit API based on the subreddit
    URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Define headers for the HTTP request
    headers = {"User-Agent": "ubuntu:0x16-api_advanced (by /u/rodgers_)"}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(
        URL,
        headers=headers,
        params={'after': after, 'limit': 10}
    )

    # If the response status code is 404 (Not Found), return
    if response.status_code == 404:
        return

    # Parse the JSON response
    data = response.json()

    # Extract information about the hot articles
    allHot = data.get("data", {}).get("children", None)
    after = data.get("data", {}).get("after", None)

    # Iterate through each hot article and count the occurrences of words
    for hotPost in allHot:
        title = hotPost.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            if word.lower() in title:
                totalIteration = 0
                for w in title:
                    if word.lower() == w:
                        totalIteration += 1
                if word.lower() not in dictWord.keys():
                    dictWord[word.lower()] = totalIteration
                else:
                    dictWord[word.lower()] += totalIteration

    # Check if there are more pages of articles (pagination)
    if after is None:
        if len(dictWord) == 0:
            pass
        else:
            # Sort and print the word counts in descending
            # order by count, then by word
            dictWord = sorted(dictWord.items(), key=lambda kv: (-kv[1], kv[0]))
            for key, value in dictWord:
                print('{}: {}'.format(key, value))
        return

    # Recursively call the function to fetch the next page of articles
    return count_words(subreddit, word_list, dictWord, after)
