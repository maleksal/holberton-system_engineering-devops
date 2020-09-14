#!/usr/bin/python3
"""
API module

"""
import json
import requests
import sys


def request_from_api(_id):
    """
    Request for a given employee ID,
    returns information about his/her TODO list progress.

    """
    # get employee name
    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + _id).json()['username']

    # get employee info
    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + _id).json()
    # Write to csv
    j_output = {_id: [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee_name
                    } for task in info]}
    # write json
    with open('{}.json'.format(_id), 'w') as json_file:
        json_file.write(json.dumps(j_output))


if __name__ == '__main__':
    employee_id = sys.argv[1]
    request_from_api(employee_id)
