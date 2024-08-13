#!/usr/bin/python3
"""
Gets first 10 hot posts on Reddit.
"""
import requests


def top_ten(subreddit):
    """Prints top 10 hot posts for a subreddit."""
    if isinstance(subreddit, str):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"limit": 10}
        req = get(url, params=params, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            data = req.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    else:
        print(None)
