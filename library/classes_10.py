
class Budget():
    
    def __init__(self, expenses_type):
        self.expenses_type = expenses_type
        self.expenses = []
        self.category = []
        self.expenses_dict = {}

    def add_expenses(self, type, expense):
    
        self.category.append(type)
        self.expenses.append(float(expense))
        self.expenses_dict[type] = float(expense)
        
        #self.write_to_file()
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
    #Reads existing data from the file if it exist
        existing_data = {}

        try:
            with open("expenses.txt", "r") as file:
                lines = [line.strip() for line in file] #goes through each lines and adds it to a list
                                                        #
            current_category = None
            for line in lines: 
                if not line: #checks if the line is empty
                    continue

                # Detect category name
                if ":" not in line and not line.startswith("$"):
                    current_category = line
                    if current_category not in existing_data:
                        existing_data[current_category] = {}
                else:
                    # Parse "type: $value"
                    item, value = line.split(":")
                    value = float(value.strip().replace("$", ""))

                    if item not in existing_data[current_category]:
                        existing_data[current_category][item] = 0

                    existing_data[current_category][item] += value

        except FileNotFoundError:
            # If file doesn't exist start with new file
            pass

        #Merges the current object's data into existing_data
        if self.expenses_type not in existing_data:
            existing_data[self.expenses_type] = {}

        for item, value in self.expenses_dict.items():
            if item not in existing_data[self.expenses_type]:
                existing_data[self.expenses_type][item] = 0

            existing_data[self.expenses_type][item] += value

        #Rewrites the file with all updated data
        with open("expenses.txt", "w") as file:
            for category, items in existing_data.items():
                file.write(f"{category}\n")
                for item, value in items.items():
                    file.write(f"{item}: ${value}\n")
                file.write("\n")

    def calc_total_balance(income):
        import project10  # so we can access budget_category

        total_expenses = 0

        for budget in project10.budget_category.values():
            total_expenses += sum(budget.expenses_dict.values())

        return income - total_expenses

    


grocery_list = Budget("grocery")

