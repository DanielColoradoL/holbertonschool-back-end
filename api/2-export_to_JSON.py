#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
import sys


if len(sys.argv) < 2:
    print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

user_info_url = "https://jsonplaceholder.typicode.com/users?id=" + employee_id
todo_url = "https://jsonplaceholder.typicode.com/todos?userId=" + employee_id

user_resp = requests.get(user_info_url)
todo_resp = requests.get(todo_url)

user_name = user_resp.json()[0]["username"]

output_dic = {}
ls = []
for entry in todo_resp.json():
    tmp_dic = {}
    tmp_dic["username"] = user_name
    tmp_dic["completed"] = entry["completed"]
    tmp_dic["task"] = entry["title"]
    ls.append(tmp_dic)

output_dic[employee_id] = ls

with open(employee_id + ".json", "w", encoding="utf-8") as f:
    json.dump(output_dic, f)
