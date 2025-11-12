class Budget:

    def __init__(self,expense_type):
        self.expense_type = expense_type
        self.expenses =[]
        self.category = []
        
    def add_expenses(self):
        expenses = []
        category= []

        i = float(input(f"\nHow many {self.expense_type} expenses would you like to input? "))
        j = 1
        while i > 0:
            itemCost = input(f"Expense #{j}: ")
            parts = itemCost.rsplit(" ", 1)
            
            if len(parts) == 2 and parts[1].isdigit():
                item = parts[0]
                cost = int(parts[1])
            else:
                while len(parts) != 2 or not parts[1].isdigit():
                    print("\n**ERROR:**\nThat was the wrong format. \nFormat: Item Cost | Example: Milk 5\n")
                    itemCost = input(f"Expense #{j}: ")
                    parts = itemCost.rsplit(" ", 1)    
                item = parts[0]
                cost = int(parts[1])    
            
                    
            self.expenses.append(int(cost))
            self.category.append(item)
            
            i -= 1
            j += 1
    
    def get_expenses(self):
        print(f"Your total {self.expense_type} expense is: ${sum(self.expenses):.2f}\n")
        return sum(self.expenses)
        
        
    def get_expense_details(self):
        for exp, cat in zip(self.expenses,self.category):
            print(f"${exp} for {cat}")
