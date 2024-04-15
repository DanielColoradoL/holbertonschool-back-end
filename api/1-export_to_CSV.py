#!/usr/bin/python3
import sys
import requests


if len(sys.argv) < 2:
    print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

user_info_url = "https://jsonplaceholder.typicode.com/users?id=" + employee_id
todo_url = "https://jsonplaceholder.typicode.com/todos?userId=" + employee_id

user_resp = requests.get(user_info_url)
todo_resp = requests.get(todo_url)

user_name = user_resp.json()[0]["username"]

with open(employee_id + ".csv", "w", encoding="utf-8") as f:
    for i, entry in enumerate(todo_resp.json()):
        string = (f'"{employee_id}",'
                  f'"{user_name}",'
                  f'"{entry["completed"]}",'
                  f'"{entry["title"]}"')
        f.write(string)
        if i + 1 < len(todo_resp.json()):
            f.write("\n")
