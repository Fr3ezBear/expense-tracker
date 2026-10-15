import sqlite3
from config import DB_NAME
import logging

logger = logging.getLogger(__name__)

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

def init_db():

    command1 = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )"""

    cursor.execute(command1)

def db_add_expense(amount, category, description, date):
    if amount <= 0:
        raise ValueError("Amount must be greater than Zero.")
    query = """
    INSERT INTO expenses
    (amount, category, description, date) 
    VALUES (?, ?, ?, ?)"""

    try:
        with connection as conn:
            conn.execute(query, (amount, category, description, date))
        return True
    except sqlite3.Error as e:
        logger.error("Amount could not be added: %s", e)
        return False

def db_list_expenses():
    query = """SELECT id, date, category, amount, description FROM expenses ORDER BY date DESC"""
    try:
        with connection as conn:
            val = conn.execute(query).fetchall()
            if len(val) == 0:
                return "No expenses yet"
            else: 
                return val
    except sqlite3.Error as e:
        logger.error("Failed to list expenses: %s", e)
        return []

def db_delete_expenses(entered_id):
    with connection as conn:
        check_id = """SELECT id FROM expenses WHERE id = ?"""
        if conn.execute(check_id, (entered_id,)).fetchone() == None:
            return "ID does not exist"
        else:
            query = """DELETE FROM expenses WHERE id = ?"""
            try:
                conn.execute(query, (entered_id,))
                return True
            except sqlite3.Error as e:
                logger.error("Expense could not be deleted: %s", e)
                return False

def db_total_expenses():
    query = """SELECT SUM(amount) FROM expenses"""
    try:
        with connection as conn:
            return conn.execute(query).fetchone()
    except sqlite3.Error as e:
        logger.error("Could not get total expenses: %s", e)
        return []