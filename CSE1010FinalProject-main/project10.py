
from tkinter import *
from library import functions
from library.classes_10 import Budget

budget_category = {}

def main(budget_name):      
    budget_category[budget_name] = Budget(budget_name)

if __name__ == "__main__":
    main()




