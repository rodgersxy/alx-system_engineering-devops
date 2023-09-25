#!/usr/bin/python3
"""
script using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


def main():
    """
    Check if the correct number of command-line arguments are provided
    """
    if len(argv) != 2:
        return

    """fetch employee data"""
    employee_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))

    employee_data = employee_response.json()

    """Fetch TODO list data for the employee"""
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1]))
    todos_data = todos_response.json()

    completed = []
    for task in todos_data:
        if task["completed"] is True:
            completed.append(task)

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee_data["name"], len(completed), len(todos_data)))
    for task in completed:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    main()
