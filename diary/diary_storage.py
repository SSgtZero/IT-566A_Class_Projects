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
        os.makedirs(data_dir_path)
    return data_dir_path


def get_diary_file_path(file_name):
    """Return the full path to a diary file inside the data directory."""
    return os.path.join(get_data_dir_path(), file_name)


def diary_file_exists(file_name):
    """Return True if the diary file already exists."""
    return os.path.exists(get_diary_file_path(file_name))


def create_diary_file(file_name):
    """Create the diary file if it does not already exist."""
    with open(get_diary_file_path(file_name), 'a', encoding=FILE_ENCODING):
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
    return datetime.now().strftime(DATE_FORMAT)


def add_entry(file_name, entry_date, entry_text):
    """Append one entry as a single line at the end of the diary file."""
    entry_text = entry_text.replace('\n', ' ')
    with open(get_diary_file_path(file_name), 'a', encoding=FILE_ENCODING) as f:
        f.write(f'{entry_date}{FIELD_SEPARATOR}{entry_text}\n')


    def read_entries(file_name):
         """Return all entries in the diary file as (date, text) tuples."""
         entries = []
         with open(get_diary_file_path(file_name), 'r', encoding=FILE_ENCODING) as f:
             for line in f:
                 line = line.strip()
                 if FIELD_SEPARATOR in line:
                     entry_date, entry_text = line.split(FIELD_SEPARATOR, 1)
                     entries.append((entry_date, entry_text))
         return entries

    
    def filter_entries_by_date(entries, entry_date):
        """Return only the entries that match entry_date."""
        return [entry for entry in entries if entry[0] == entry_date]