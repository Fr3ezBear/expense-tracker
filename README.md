# Expense Tracker

A simple command-line expense tracker built with Python and SQLite.

## Features

- Add an expense (amount, category, description, date)
- List all expenses, newest first
- Delete an expense by ID
- View total spending

## Tech Stack

- Python 3
- SQLite (via the built-in `sqlite3` module)
- [tabulate](https://pypi.org/project/tabulate/) for table output

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/Fr3ezBear/expense-tracker.git
   cd expense-tracker
   ```

2. Install the dependency:

   ```bash
   pip install tabulate
   ```

3. Run the app:

   ```bash
   python main.py
   ```

The database file is created automatically on first run. Its name is set by `DB_NAME` in `config.py`.

## Usage

Run the program and pick an option from the menu to add, list, or delete expenses, or to see your total.

## Notes

- Amounts must be greater than zero.
- Database errors are logged instead of crashing the app.

## Author

[Fr3ezBear](https://github.com/Fr3ezBear)
