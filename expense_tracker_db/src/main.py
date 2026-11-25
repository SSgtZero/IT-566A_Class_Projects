"""Entry point for the Expense Tracker application."""

from expense_menu import ExpenseMenu


def main():
    """Execute main program."""
    menu = ExpenseMenu()
    menu.start_application()


# Call main() if this is the main execution module
if __name__ == '__main__':
    main()