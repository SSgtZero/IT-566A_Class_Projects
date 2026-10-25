"""expense_menu module contains the ExpenseMenu class."""
from datetime import datetime

import expense_files
from expense_filter import filter_expenses


class ExpenseMenu:
    """Console menu to enter, filter, save, open, and export expenses."""


    def __init__(self):
        """Initialize the expense list and menu choice constants."""
        self.expenses = []
        self._ADD_EXPENSE = '1'
        self._LIST_EXPENSES = '2'
        self._FILTER_EXPENSES = '3'
        self._SAVE_FILE = '4'
        self._OPEN_FILE = '5'
        self._EXPORT_CSV = '6'
        self._EXIT = '7'


    def display_menu(self):
        """Print the menu."""
        print('\n===== EXPENSE TRACKER =====')
        print('1. Add expense')
        print('2. List all expenses')
        print('3. Filter expenses')
        print('4. Save to JSON file')
        print('5. Open JSON file')
        print('6. Export to CSV file')
        print('7. Exit')


    def start_application(self):
        """Process menu choices until the user chooses Exit."""
        while True:
            self.display_menu()
            choice = input('Enter menu choice: ').strip()
            try:
                match choice:
                    case self._ADD_EXPENSE:
                        self.add_expense()
                    case self._LIST_EXPENSES:
                        self.print_expenses(self.expenses)
                    case self._FILTER_EXPENSES:
                        self.filter_and_print_expenses()
                    case self._SAVE_FILE:
                        self.save_file()
                    case self._OPEN_FILE:
                        self.open_file()
                    case self._EXPORT_CSV:
                        self.export_csv()
                    case self._EXIT:
                        return
                    case _:
                        print(f'WARNING: {choice} is an invalid choice!')
            except (OSError, Exception) as e:
                print(f'Problem with file I/O: {e}')


    def add_expense(self):
        """Prompt for an expense and add it to the list."""
        expense = {}
        expense['date'] = self.prompt_for_date('Date (YYYY-MM-DD): ')
        expense['category'] = input('Category: ').strip()
        expense['description'] = input('Description: ').strip()
        expense['amount'] = self.prompt_for_amount('Amount: ')
        self.expenses.append(expense)


    def filter_and_print_expenses(self):
        """Prompt for filters and print the matching expenses."""
        print('Press Enter to skip a filter.')
        start_date = self.prompt_for_date('Start date: ', required=False)
        end_date = self.prompt_for_date('End date: ', required=False)
        category = input('Category: ').strip()
        self.print_expenses(
            filter_expenses(self.expenses, start_date, end_date, category))


    def print_expenses(self, expenses):
        """Print expenses sorted by date, followed by the total."""
        total = 0
        for e in sorted(expenses, key= lambda e: e['date']):
            print(f"{e['date']} {e['category']: <15} "
                  f"{e['description']: <25} ${e['amount']:>9.2f}")
            total += e['amount']
        print(f'{len(expenses)} expense(s) Total: ${total:.2f}')


    def save_file(self):
        """Save the expense list to a JSON file."""
        filename = input('Filename to save: ').strip()
        file_path = expense_files.get_file_path(filename, '.json')
        expense_files.save_json(self.expenses, file_path)
        print(f'Saved to {file_path}')


    def open_file(self):
        """Open a JSON file and replace the expense list."""
        filename = input('Filename to open: ').strip()
        file_path = expense_files.get_file_path(filename, '.json')
        self.expenses = expense_files.open_json(file_path)
        print(f'Opened {file_path}')


    def export_csv(self):
        """Export the expense list to a CSV file."""
        filename = input('CSV filename: ').strip()
        file_path = expense_files.get_file_path(filename, '.csv')
        expense_files.export_csv(self.expenses, file_path)
        print(f'Exported to {file_path}')


    def prompt_for_date(self, prompt, required=True):
        """Prompt until the user enters a valid YYYY-MM-DD date."""
        while True:
            text = input(prompt).strip()
            if not text and not required:
                return ''
            try:
                date = datetime.strptime(text, '%Y-%m-%d')
                return date.strftime('%Y-%m-%d')
            except ValueError:
                print('Invalid date. Use YYYY-MM-DD, for example 2026-10-23.')


    def prompt_for_amount(self, prompt):
        """Prompt until the user enters a number."""
        while True:
            try:
                return round(float(input(prompt)), 2)
            except ValueError:
                print('Invalid amount. Enter a number, for example 12.50')    