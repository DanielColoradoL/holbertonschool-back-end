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

user_name = user_resp.json()[0]["name"]
total_t = len(todo_resp.json())
completed_t = []
for entry in todo_resp.json():
    if entry["completed"] is True:
        completed_t.append(entry["title"])

done_t = len(completed_t)

if user_resp:
    print(f"Employee {user_name} is done with tasks({done_t}/{total_t}):")
    for task in completed_t:
        print("\t " + task)
