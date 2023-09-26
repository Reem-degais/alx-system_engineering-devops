#!/usr/bin/python3
""" export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    rest_api = "https://jsonplaceholder.typicode.com/"
    user_req = requests.get(rest_api + "users/{}".format(argv[1])).json()
    todos = requests.get(rest_api + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_req.get("username")
            } for t in todos]}, jsonfile)
