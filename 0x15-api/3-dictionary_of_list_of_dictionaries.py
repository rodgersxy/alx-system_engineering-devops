#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


def main():
    """
    Fetch employee data from the API
    """

    employees_response = requests.get(
            "https://jsonplaceholder.typicode.com/users")
    employees = employees_response.json()

    all_tasks = {}

    for employee in employees:
        todos_response = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}/todos".
                format(employee["id"]))
        todos = todos_response.json()

        employee_tasks = []
        for task in todos:
            employee_tasks.append(
                {"username": employee["username"],
                 "task": task["title"], "completed": task["completed"]
                 })
        all_tasks[employee["id"]] = employee_tasks
    with open("todo_all_employees.json", 'w',
              newline='', encoding='utf-8') as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    main()
