#clears terminal
print("\x1b[H\x1b[2J", end="")

print("Hey there, this is BudgetBuddy! Your personal Budgeting Assistant.")

name = input("Enter your name: ")

print(f"\nHey {name}, This is BudgetBuddy! Your personal Budgeting Assistant!")


from library import functions

income = float(input("\nWhat is your monthly income? (Numbers Only!)\n"))

## Project 9
from library.classes_9 import Budget

cat1 = Budget("Groceries")
cat2 = Budget("Car")

cat1.add_expenses()
cat2.add_expenses()

total_expenses = []
total_expenses.extend(cat1.expenses)
total_expenses.extend(cat2.expenses)

print("")

# Project 8 Code
cat1.get_expense_details()
cat2.get_expense_details()

# Project 7 Code
balance = functions.calc_balance(income,sum(total_expenses))

print(f"Your total expenses are: ${sum(total_expenses):.2f}")
print(f"Your total balance is ${balance}")

# Project 7 Code
functions.financial_status(balance)
