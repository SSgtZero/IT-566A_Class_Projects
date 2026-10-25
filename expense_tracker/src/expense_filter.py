"""expense_filter module filters expenses by date range and/or category."""


def filter_expenses(expenses, start_date='', end_date='', category=''):
    """Return the expenses that match every filter that is not blank."""
    results = []
    for expense in expenses:
        if start_date and expense['date'] < start_date:
            continue
        if end_date and expense['date'] > end_date:
            continue
        if category and expense['category'].lower() != category.lower():
            continue
        results.append(expense)
    return results