#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot
    posts listed for a given subreddit"""
    url = 'https://www.reddit.com'
    api_url = '{}/r/{}/hot.json'.format(url, subreddit)

    user_agent = {'User-Agent': 'Python/requests'}
    top = {'limit': '10'}
    res = requests.get(api_uri, headers=user_agent,
                       params=top, allow_redirects=False)
    if res.status_code in [302, 404]:
        print('None')
    else:
        if res.json().get('data') and res.json().get('data').get('children'):
            hot = res.json().get('data').get('children')
            for post in hot:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
