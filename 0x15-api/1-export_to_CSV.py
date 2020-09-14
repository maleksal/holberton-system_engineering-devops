#!/usr/bin/python3
"""
API module

"""
import requests
import sys
import csv


def request_from_api(_id):
    """
    Request for a given employee ID,
    returns information about his/her TODO list progress.

    """
    # get employee name
    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + _id).json()['name']

    # get employee info
    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + _id).json()
    # Write to csv
    with open('{}.csv'.format(_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow([
                _id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ]) for task in info]


if __name__ == '__main__':
    employee_id = sys.argv[1]
    request_from_api(employee_id)
