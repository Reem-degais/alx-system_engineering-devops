#!/usr/bin/python3
""" export data in the CSV format"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    rest_api = "https://jsonplaceholder.typicode.com/"
    user_req = requests.get(rest_api + "users/{}".format(argv[1])).json()
    todos = requests.get(rest_api + "todos", params={"userId": argv[1]}).json()

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [argv[1], user_req.get("username"), t.get("completed"),
             t.get("title")]
         ) for t in todos]
