#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit"""
    url = 'https://www.reddit.com'
    api_uri = '{}/r/{}/about.json'.format(url, subreddit)

    
    user_agent = {'User-Agent': 'Python/requests'}
    res = requests.get(api_uri, headers=user_agent,
                       allow_redirects=False)
  
    if res.status_code in [302, 404]:
        return 0
    
    return res.json().get('data').get('subscribers')
