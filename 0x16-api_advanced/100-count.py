#!/usr/bin/python3
""" Recursive API calls to Redit & counts occurrences
"""
import requests


def count_words(subreddit, word_list, key_words={}, count={}, after=None):
    """ returns count of occurrence of words
    """
    if not count:
        key_words = {word.lower(): 0 for word in word_list}
        word_list = [word.lower() for word in word_list]
        count = {word.lower(): word_list.count(word.lower())
                 for word in word_list}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    req = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get('data')
        after = data.get('after')
        posts = data.get('children')

        for post in posts:
            title = post.get('data').get('title').lower()
            words = title.split()
            for word in key_words.keys():
                key_words[word] += words.count(word)

        if after:
            return count_words(subreddit, word_list, key_words, count, after)
        else:
            for key in key_words.keys():
                key_words[key] *= count[key]
            key_words = sorted(key_words.items(),
                               key=lambda item: (-item[1], item[0]))
            for item in key_words:
                if item[1] > 0:
                    print("{}: {}".format(item[0], item[1]))
