#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
his/her TODO list progress.
Python script to export data in the CSV format.
"""

import csv
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

    """Create a CSV file"""
    csv_file = "{}.csv".format(argv[1])
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        field_name = csv.writer(f, quoting=csv.QUOTE_ALL)
        for tasks in todos:
            field_name.writerow(
                [argv[1], employee_data['username'],
                 tasks["completed"], tasks["title"]])


if __name__ == "__main__":
    main()
