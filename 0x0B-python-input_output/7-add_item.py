#!/usr/bin/python3
"""This Script add items provided as
   command line arguments to a Python
   list and save them in a JSON file.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_all_args(args, filename):
    """Adds all arguments to a Python list
       and save them as a JSON file
    """
    items = []
    try:
        if os.path.exists(filename):
            items = load_from_json_file(filename)

    except Exception:
        items = []

    for item in args:
        items.append(item)
    save_to_json_file(items, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_all_args(args, filename)
