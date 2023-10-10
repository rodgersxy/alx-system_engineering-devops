#!/usr/bin/python3
"""
A function that Queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
# Import the requests library, which allows making HTTP requests
import requests

# Define custom User-Agent headers to identify the client
headers = {"User-Agent": "ubuntu:0x16-api_advanced (by /u/rodgers_)"}


def recurse(subreddit, hot_list=[], after=None):
    # Construct the URL to query the Reddit API for
    # hot articles in a subreddit
    # The 'after' parameter is used for pagination
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
          .format(subreddit, after)

    # Send a GET request to the constructed URL with custom headers
    request = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if request.status_code == 200:
        # Parse the JSON response and iterate through the list of posts
        for children in request.json().get("data").get("children"):
            # Append the title of each post to the 'hot_list' variable
            hot_list.append(children.get("data").get("title"))

        # Get the 'after' token from the response for pagination
        after = request.json().get("data").get("after")

        # If there's no 'after' token, it means we've reached the end
        # of the posts
        if not after:
            return hot_list

        # Recursively call the 'recurse' function with the 'after'
        # token to fetch more posts
        return recurse(subreddit, hot_list, after)
    else:
        # If the request was not successful, return "None" to indicate an issue
        return None
