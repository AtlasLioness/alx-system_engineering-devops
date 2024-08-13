#!/user/bin/python3
"""Recursive API call to Reddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list w/ titles of all hot articles for a given subreddit."""
    if isinstance(subreddit, str):
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {'after': after, 'limit': 100}

        response = requests.get(url, params=params, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data')
            after = data.get('after')
            posts = data.get('children', [])

            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
