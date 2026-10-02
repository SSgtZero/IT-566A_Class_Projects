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