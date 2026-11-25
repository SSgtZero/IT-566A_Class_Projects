"""expense_files module saves, opens, and exports expense files."""

import csv
import json
import os

DATA_DIR = 'data'
FIELDNAMES = ['date', 'category', 'description', 'amount']


def get_file_path(filename, extension):
    """Return the path to filename in the data directory."""
    data_dir_path = os.path.join(os.getcwd(), DATA_DIR)
    if not os.path.exists(data_dir_path):
        os.mkdir(data_dir_path)
    if not filename.endswith(extension):
        filename = filename + extension
    return os.path.join(data_dir_path, filename)


def save_json(expenses, file_path):
    """Convert the expense list to JSON and write it to file."""
    json_string = json.dumps({'expenses': expenses}, indent=4)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_string)


def open_json(file_path):
    """Read a JSON file and return the expense list."""
    with open(file_path, 'r', encoding='utf-8') as f:
        json_string = f.read()
    return json.loads(json_string)['expenses']


def export_csv(expenses, file_path):
    """Write the expense list to a CSV file EXcel can open."""
    with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)