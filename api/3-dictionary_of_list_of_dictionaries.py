#!/usr/bin/python3
import json
import requests


user_info_url = "https://jsonplaceholder.typicode.com/users"
todo_url = "https://jsonplaceholder.typicode.com/todos"

user_resp = requests.get(user_info_url)
todo_resp = requests.get(todo_url)


output_dic = {}

for user in user_resp.json():
    user_id = user.get("id")
    user_name = user.get("username")
    ls = []
    for entry in todo_resp.json():
        if user_id != entry["userId"]:
            continue
        tmp_dic = {}
        tmp_dic["username"] = user_name
        tmp_dic["completed"] = entry.get("completed")
        tmp_dic["task"] = entry.get("title")
        ls.append(tmp_dic)
    output_dic[user_id] = ls

with open(".todo_all_employees.json", "w", encoding="utf-8") as f:
    json.dump(output_dic, f)
