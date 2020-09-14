#!/usr/bin/python3
"""
API module

"""
import json
import requests
import sys


def request_from_api():
    """
    Get all employees data: username, todo, todo status.

    """
    main_url = 'https://jsonplaceholder.typicode.com'
    json_database = {}
    # get all users
    all_users = requests.get(main_url + '/users').json()
    for user in all_users:
        # get employee name
        user_id = str(user.get('id'))
        employee_name = requests.get(
            main_url + '/users/' + user_id).json()['username']
        # get employee info
        info = requests.get(main_url + '/todos?userId=' + user_id).json()
        # Write to database
        json_database[user_id] = [{
                    "username": employee_name,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                    } for task in info]
    # write json
    with open('todo_all_employees.json', 'w') as json_file:
        json_file.write(json.dumps(json_database))


if __name__ == '__main__':
    request_from_api()
