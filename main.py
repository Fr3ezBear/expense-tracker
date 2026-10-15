from database import *
from datetime import date, datetime
import logging
import tabulate
import sys

logger = logging.getLogger(__name__)

class ExpenseTracker:
    def __init__(self):
        init_db()
        self.menu()

    def parse_date(self, text):
        try:
            return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
        except ValueError:
            return None


    def show_expenses(self):
        rows = db_list_expenses()
        if type(rows) == str:
            print(rows)
        else:
            print(tabulate.tabulate(rows, headers=["ID", "Date", "Category", "Amount", "Description"]))

    def add_expense(self):

        print("Adding Expense: ")
        try:
            amount = float(input("Enter amount: "))
            
            category = input("Enter category: ")
    
            desc = input("Enter description: ")
    
            given_date = input("Enter date or skip to default to today: ")
            if self.parse_date(given_date) == None:
                given_date = date.today().isoformat()
            else:
                given_date = self.parse_date(given_date)
            db_add_expense(amount, category, desc, given_date)
    
            print("Expense added successfully")
            
        except ValueError as e:
            print("Adding expenses failed: %s", e)

    def delete_expense(self):
        try:
            id_to_affect = int(input("Enter id to delete: "))
            result = db_delete_expenses(id_to_affect)
            if type(result) == str:
                print(result)
            else:
                print("Expense deleted successfully")
        except ValueError as e:
            logger.error("Invalid input for id: %s", e)


    def total_expense(self):
        print("Total expenses:", db_total_expenses()[0])
    

    def menu(self):
        while True:
            print("\n1. Add expense")
            print("2. List expenses")
            print("3. Delete expense")
            print("4. Totals")
            print("5. Quit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.show_expenses()
            elif choice == "3":
                self.delete_expense()
            elif choice == "4":
                self.total_expense()
            elif choice == "5":
                print("Goodbye!")
                sys.exit(0) 
            else:
                print("Invalid choice, enter a number from 1 to 5.")


if __name__ == "__main__":
    ExpenseTracker().menu()