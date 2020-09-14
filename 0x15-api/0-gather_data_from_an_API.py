#!/usr/bin/python3
"""
API module

"""
import requests
import sys


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
    completed_t = 0
    all_t = 0
    titels = []
    for el in info:
        if el.get("completed"):
            titels.append(el.get("title"))
            completed_t += 1
        all_t += 1
    print(
        'Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                        completed_t,
                                                        all_t))
    for i in titels:
        print('\t {}'.format(i))


if __name__ == '__main__':
    employee_id = sys.argv[1]
    request_from_api(employee_id)
