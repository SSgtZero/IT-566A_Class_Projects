"""Diary file storage functions.
Each diary entry is saved as one line in a text file:
    YYYY-MM-DD|ENTRY TEXT
"""

import os
from datetime import datetime

DATA_DIR = 'data'
DATE_FORMAT = '%Y-%m-%d'
FIELD_SEPARATOR = '|'
FILE_ENCODING = 'utf-8'


def get_data_dir_path():
    """Return the path to the data directory, creating it if needed."""
    data_dir_path = os.path.join(os.getcwd(), DATA_DIR)
    if not os.path.exists(data_dir_path):
        os.makeddirs(data_dir_path)
    return data_dir_path

def get_diary_file_path (file name):
    """Return the full path to a diary file inside the data directory."""
    return os.path.join(get_data_dir_path(), file_name)

def diary_file_exists(file_name):
    """Return True if the diary file already exists."""
    return
os.path.exists(get_diary_file_path(file_name))

def create_diary_file(file_name):
    """Create the diary file if it does not already exists."""
    with open(get_diary_file_path(file_name),
'a', encoding=FILE_ENCODING):
        pass

def is_valid_date(date_text):
    """Return True if date_text is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_text, DATE_FORMAT)
        return True
    except ValueError:
        return False

def get_today():
    """Return today's date as a YYYY-MM-DD string."""
    return
datetime.now().strftime(DATE_FORMAT)