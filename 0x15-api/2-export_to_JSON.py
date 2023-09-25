#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
his/her TODO list progress.
Python script to export data in the CSV format.
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

    employee_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    employee_data = employee_response.json()

    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                 argv[1]))
    todos = todos_response.json()

    list_task = []

    for task in todos:
        list_task.append(
            {"task": task["title"], "completed": task["completed"],
             "username": employee_data["username"]})

    """Create a JSON file with the employee's tasks"""
    json_file = "{}.json".format(argv[1])
    with open(json_file, 'w', newline='', encoding='utf-8') as file:
        json.dump({employee_data["id"]: list_task}, file)


if __name__ == "__main__":
    main()
