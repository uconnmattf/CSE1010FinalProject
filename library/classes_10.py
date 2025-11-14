
class Budget():
    
    def __init__(self, expenses_type):
        self.expenses_type = expenses_type
        self.expenses = []
        self.category = []
        self.expenses_dict = {}

    def add_expenses(self):
        
        print()

        while True:
            try:
                expenselist = int(input(f"How many expenses do you want to specify for {self.expenses_type}: "))
                break
            except Exception:
                print("Please input an integer number.")
            
        for i in range(expenselist):
            while True:
                try:
                    type, expense = input(f"Enter expense {i+1} in type cost format(e.g milk 12): ").split()
                    self.category.append(type)
                    self.expenses.append(float(expense))
                    self.expenses_dict[type] = float(expense)
                    break
                except Exception:
                    print("Please input expense in type cost format(e.g milk 12).")
        
        self.write_to_file()
        
        return self.expenses

    def get_expenses(self):
        print(f"You spent ${sum(self.expenses)} on {self.expenses_type}.\n")


    def get_expense_details(self):
        
        print()

        print(f"Expenses for {self.expenses_type}:")
        for i in range(len(self.expenses)):
            print(f"{self.category[i]}: ${self.expenses[i]}")


    def calc_balance(self):

        while True:
            try:
                self.income = float(input("\nEnter your income: "))
                break
            except Exception:
                print("Invalid input.")
              
        
        
        self.balance = self.income - sum(self.expenses)

        
        print(f"Your balance is {self.balance}.")
        print()


        if self.balance > 0:
            print("Great! You are saving money!")
        elif self.balance == 0:
            print("You are breaking even.")
        else:
            print("**WARNING** You are overspending!") 
    
    
    def write_to_file(self):
        with open("expenses.txt", "a") as file:  
            file.write(f"{self.expenses_type}\n")
            
            for type, expense in self.expenses_dict.items():
                file.write(f"{type}: ${expense}\n")

            file.write("\n")  

    def calc_total_balance(*budgets):
        
        print()

        while True:
            try:
                income = float(input("Enter your total income: "))
                break
            except Exception:
                print("Invalid input")

        total_expenses = sum(sum(current_budget.expenses) for current_budget in budgets)
        balance = income - total_expenses

        print(f"\nYour total balance after all expenses is: ${balance:.2f}")

        if balance > 0:
            print("Great! You are saving money!")
        elif balance == 0:
            print("You are breaking even.")
        else:
            print("**WARNING** You are overspending!")

    


grocery_list = Budget("grocery")

