#!/usr/bin/python3
"""
queries & returns nb of subs of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns nb of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:alx.api.advanced:v1.0.0 (by u/Elegant_Student_3795)"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json().get("data")
        return results.get("subscribers")
