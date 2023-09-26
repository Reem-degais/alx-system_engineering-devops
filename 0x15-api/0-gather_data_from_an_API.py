#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv


rest_api = "https://jsonplaceholder.typicode.com/"

if __name__ == '__main__':
    user_req = requests.get('{}users/{}'.format(rest_api, argv[1])).json()
    todos = requests.get(rest_api + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_req.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
