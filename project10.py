
from tkinter import *
from library import functions
from library.classes_10 import Budget

def main(name):

    print(f"Hey {name}, this is BudgetBuddy! Your personal Budgeting Assistant.")

    grocery = Budget("Grocery")
    Toyota_Camry = Budget("Car")

    grocery.add_expenses()
    Toyota_Camry.add_expenses()

    grocery.get_expense_details()
    Toyota_Camry.get_expense_details()

    Budget.calc_total_balance(grocery, Toyota_Camry)


if __name__ == "__main__":
    main()




