"""Main entry point for the diary application."""

import diary_storage

_DESIGNATE_FILE = '1'
_LOAD_FILE = '2'
_ADD_ENTRY = '3'
_PRINT_ALL = '4'
_PRINT_BY_DATE = '5'
_QUIT = '6'

DEFAULT_DIARY_FILE = 'diary.txt'


def print_menu(diary_file):
    """Print the menu along with the diary file currently in use."""
    print()
    print(f'Current diary file: {diary_file}')
    print('1. Designate a diary file (new or existing)')
    print('2. Load a different existing diary file')
    print('3. Add an entry')
    print('4. Print all entries')
    print('5. Print entries for one date')
    print('6. Quit')


def print_entries(entries):
    """Print each entry on its own line."""
    if not entries:
        print('No entries found.')
    for entry_date, entry_text in entries:
        print(f'{entry_date}: {entry_text}')


def designate_diary_file(diary_file):
    """Let the user pick a file name; create the file if it is new."""
    file_name = input('Enter diary file name (example: diary.txt): ').strip()
    if not file_name:
        print('No file name entered.')
        return diary_file
    diary_storage.create_diary_file(file_name)
    print(f'Now using {file_name}')
    return file_name


def load_diary_file(diary_file):
    """Switch to a diary file that already exists."""
    file_name = input('Enter name of the diary file to load: ').strip()
    if not diary_storage.diary_file_exists(file_name):
        print(f'Could not find {file_name}')
        return diary_file
    print(f'Loaded {file_name}')
    return file_name


def add_entry(diary_file):
    """Ask for a date and some text, then save the entry."""
    entry_date = input('Date (YYYY-MM-DD, or press Enter for today): ').strip()
    if not entry_date:
        entry_date = diary_storage.get_today()
    if not diary_storage.is_valid_date(entry_date):
        print('Invalid date. Use the format YYYY-MM-DD.')
        return
    entry_text = input('Entry: ').strip()
    if not entry_text:
        print('Entry was empty. Nothing saved.')
        return
    diary_storage.add_entry(diary_file, entry_date, entry_text)
    print('Entry saved.')


def print_entries_by_date(diary_file):
    """Ask for a date and print only the entries for that date."""
    entry_date = input('Date to show (YYYY-MM-DD): ').strip()
    if not diary_storage.is_valid_date(entry_date):
        print('Invalid date. Use the format YYYY-MM-DD.')
        return
    entries = diary_storage.read_entries(diary_file)
    print_entries(diary_storage.filter_entries_by_date(entries, entry_date))


def main():
    """Run the menu loop until the user chooses to quit."""
    diary_file = DEFAULT_DIARY_FILE

    try:
        diary_storage.create_diary_file(diary_file)
        menu_choice = ''
        while menu_choice != _QUIT:
            print_menu(diary_file)
            menu_choice = input('Enter your choice (1-6): ').strip()

            if menu_choice == _DESIGNATE_FILE:
                diary_file = designate_diary_file(diary_file)
            elif menu_choice == _LOAD_FILE:
                diary_file = load_diary_file(diary_file)
            elif menu_choice == _ADD_ENTRY:
                add_entry(diary_file)
            elif menu_choice == _PRINT_ALL:
                print_entries(diary_storage.read_entries(diary_file))
            elif menu_choice == _PRINT_BY_DATE:
                print_entries_by_date(diary_file)
            elif menu_choice == _QUIT:
                print('Goodbye!')
            else:
                print(f'WARNING: {menu_choice} is an invalid choice!')
    except (OSError, Exception) as e:
        print(f'Error! {e}')


if __name__ == '__main__':
    main()