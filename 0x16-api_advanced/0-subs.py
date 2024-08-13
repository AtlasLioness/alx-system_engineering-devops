#!/usr/bin/python3
"""
queries & returns nb of subs of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns nb of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
