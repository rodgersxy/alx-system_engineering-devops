#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """
    Adds item into a list basd=ed on the keywords
    """
    # Check if there are any hot posts left to process
    if len(hot_posts) == 0:
        return
    # Split the title into words and iterate through them
    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """
    Queries the Reddit API
    Define a function to recursively query the Reddit API for hot post
    """
    # Set the user agent
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    # Define query parameters, including 'after' for pagination
    params = {
        'after': after
    }

    # Define the Reddit API URL for the specified subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """
    Init function
    Check if a dictionary is provided, and if not, create an empty one
    """
    if dictionary is None:
        dictionary = {}

    for word in word_list:
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 0

    recurse(subreddit, dictionary)

    # Sort the word counts in descending order and print them
    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}: {}".format(item[0], item[1]))
