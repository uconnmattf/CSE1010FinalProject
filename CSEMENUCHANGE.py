from tkinter import *
from PIL import Image, ImageTk
import project10
from library.classes_10 import Budget

class BudgetBuddyApp:
    def __init__(self, menu):
        self.menu = menu
        self.menu.geometry("1024x768")
        self.menu.title("Budget Buddy")
        self.load_expenses_from_file("expenses.txt")

        # temp images please ignore
        self.temp_image1 = ImageTk.PhotoImage(Image.open("Images/jtempimage2.png").resize((200, 200)))
        self.temp_image2 = ImageTk.PhotoImage(Image.open("Images/jtempimage1.png").resize((250, 250)))
        self.title_photo = PhotoImage(file="Images/Budget_Icon.png")
        self.menu.iconphoto(True, self.title_photo)

        # Tracks currently displayed widgets
        self.current_widgets = []

        # Store user data
        self.user_name = ""
        self.new_category_name = ""

        # Shows the screen where you input your name
        self.show_name_input_screen()

    
    def load_expenses_from_file(self, filename="expenses.txt"):
        
        project10.budget_category = {}
        
        try:
            with open(filename, "r") as file:
                lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty data.")
            return

        current_category = None
        for line in lines:
            if line == "":
                current_category = None
                continue
            
            if current_category is None:
                # This is a category line
                current_category = line
                if current_category not in project10.budget_category:
                    # Create a new Budget instance if it doesn't exist
                    project10.budget_category[current_category] = Budget(current_category)
            else:
                if ":" not in line:
                    print(f"Skipping malformed line: {line}")
                    continue
                try:
                    expense_type, expense_cost = line.split(":", 1)  # split only on first ":"
                    expense_type = expense_type.strip()
                    expense_cost = expense_cost.strip().replace("$", "")  # remove any $ sign

                    if expense_cost == "":
                        expense_cost = 0.0
                    else:
                        expense_cost = float(expense_cost)
                    
                    project10.budget_category[current_category].add_expenses(expense_type, expense_cost)
                except ValueError:
                    print(f"Skipping line with invalid number: {line}")
    
    
    # hides the current widgets on screen
    def clear_screen(self):
        for widget in self.current_widgets:
            widget.pack_forget()
        self.current_widgets = []

    # Name input screen
    def show_name_input_screen(self):
        self.clear_screen()

        self.title_label = Label(self.menu, 
                                 text="Budget Buddy", 
                                 font=("Arial",40,"bold"), 
                                 fg="#ADD8E6",
                                 relief=RAISED, 
                                 bd=10, 
                                 padx=20, 
                                 pady=20)
        self.title_label.pack()

        self.name_label = Label(self.menu, 
                                text="Enter your name.", 
                                font=("Arial",20,"bold"))
        self.name_label.pack()

        self.name_box = Entry(self.menu)
        self.name_box.pack()

        self.submit_button = Button(self.menu, 
                                    text="Submit", 
                                    command=self.submit_name)
        self.submit_button.pack()

        self.current_widgets = [self.title_label, self.name_label, self.name_box, self.submit_button]

    # Handles name submission
    def submit_name(self):
        self.user_name = self.name_box.get()
        self.show_main_menu()

    # Main menu screen
    def show_main_menu(self):
        self.clear_screen()

        self.greeting = Label(self.menu, 
                              text=f"Hello {self.user_name}, this is BudgetBuddy!", 
                              font=("Arial",20,"bold"), 
                              fg="#ADD8E6")
        self.greeting.pack()

        self.prompt = Label(self.menu, 
                            text="What would you like to do?", 
                            font=("Arial",20,"bold"))
        self.prompt.pack()

        self.btn_new_category = Button(self.menu, text="Create a new expense category", 
                                       width=25, 
                                       height=3,
                                       command=self.show_new_category_screen)
        self.btn_new_category.pack(side=LEFT, padx=10)
        
        self.btn_add_expenses = Button(self.menu, 
                                       text="Add expenses into a category", 
                                       width=25, 
                                       height=3,
                                       command=self.select_add_expenses_screen)
        self.btn_add_expenses.pack(side=LEFT, padx=10)
        
        self.btn_display_expenses = Button(self.menu, 
                                           text="Display expenses", 
                                           width=25, 
                                           height=3,
                                           command=self.show_all_expenses)
        self.btn_display_expenses.pack(side=LEFT,padx=10)
        
        self.btn_financial_status = Button(self.menu, 
                                           text="View financial status", 
                                           width=25, 
                                           height=3,
                                           command=self.collect_financial_status)
        self.btn_financial_status.pack(side=LEFT,padx=10)

        for btn in [self.btn_new_category, self.btn_add_expenses, self.btn_display_expenses, 
                    self.btn_financial_status]:
            btn.pack(pady=5)

        self.current_widgets = [self.greeting, self.prompt, self.btn_new_category, 
                                self.btn_add_expenses, self.btn_display_expenses, 
                                self.btn_financial_status]

    # New category screen
    def show_new_category_screen(self):
        self.clear_screen()

        self.label_new_category = Label(self.menu, 
                                        text="Enter the name of the new category.", 
                                        font=("Arial",20,"bold"))
        self.label_new_category.pack()

        self.entry_new_category = Entry(self.menu, 
                                        width=25)
        self.entry_new_category.pack()

        self.confirm_btn = Button(self.menu, 
                                  text="Confirm", 
                                  width=20, 
                                  height=3, 
                                  command=self.confirm_new_category)
        self.confirm_btn.pack()

        self.current_widgets = [self.label_new_category, self.entry_new_category, self.confirm_btn]

    # Confirm new category
    def confirm_new_category(self):
        self.new_category_name = self.entry_new_category.get()
        project10.main(self.new_category_name)
        self.show_category_confirmation()

    # Confirmation screen
    def show_category_confirmation(self):
        self.clear_screen()

        self.confirmation_label = Label(self.menu, 
                                        text=f"{self.new_category_name} has been added as a category.", 
                                        font=("Arial",20,"bold"))
        self.confirmation_label.pack()

        self.btn_add_another = Button(self.menu, 
                                      text="Add another category?", 
                                      width=25, 
                                      height=3,
                                      command=self.show_new_category_screen)

        self.btn_return_menu = Button(self.menu, 
                                      text="Return to Menu", 
                                      width=25, 
                                      height=3,
                                      command=self.show_main_menu)

        self.btn_add_another.pack(pady=5)
        self.btn_return_menu.pack(pady=5)

        self.current_widgets = [self.confirmation_label, self.btn_add_another, self.btn_return_menu]

    #Adding expenses screen
    def select_add_expenses_screen(self):
        self.clear_screen()

        self.expense_label = Label(self.menu,
                                   text="Which category do you want to add expenses to?",
                                   font=("Arial",20,"bold"))
        self.expense_label.pack()
    
        self.current_widgets = [self.expense_label]

        for key, budget_instance in project10.budget_category.items():
            btn = Button(self.menu,
                         text=f"{key}",
                         width=25,
                         height=3,
                         command=lambda b=budget_instance: self.get_num_expense_screen(b))
            self.current_widgets.append(btn)
            btn.pack(side=LEFT , padx=10)

    def get_num_expense_screen(self, budget_instance):
        self.clear_screen()
        self.selected_budget = budget_instance

        self.expense_num_label = Label(menu,
                                       text="How many expenses do you want to record",
                                       font=("Arial",20,"bold"))
        self.expense_num_label.pack()

        self.get_expense_num = Entry(menu)
        self.get_expense_num.pack()

        self.submit_expense_num = Button(menu,
                                         text="Submit",
                                         width=25,
                                         height=3,
                                         command=self.record_expenses_screen)
        self.submit_expense_num.pack(side=LEFT, padx=10)

        self.current_widgets = [self.expense_num_label, self.get_expense_num, self.submit_expense_num]

    def record_expenses_screen(self):
        self.clear_screen()

        self.expense_entries = []

        self.expensenum = int(self.get_expense_num.get())        

        for i in range(self.expensenum):
            type_label = Label(menu,
                                    text=f"Enter expense {i+1} type",
                                    font=("Arial",20))
            type_label.pack()
            self.current_widgets.append(type_label)

            type_input = Entry(menu)
            type_input.pack()
            self.current_widgets.append(type_input)

            cost_label = Label(menu,
                                   text="Enter the cost",
                                   font=("Arial", 20))
            cost_label.pack()
            self.current_widgets.append(cost_label)

            cost_input = Entry(menu)
            cost_input.pack()
            
            self.current_widgets.append(cost_input)

            self.expense_entries.append((type_input, cost_input))
        
        self.submit_expense = Button(menu,
                                         text="Submit",
                                         width=25,
                                         height=3,
                                         command=self.save_expenses)
        self.submit_expense.pack(side=LEFT, padx=10)

        self.current_widgets.append(self.submit_expense)

    def save_expenses(self):
        for type_input, cost_input in self.expense_entries:
            expense_type = type_input.get()
            expense_cost = float(cost_input.get())
            self.selected_budget.add_expenses(expense_type, expense_cost) 
        
        self.save_expenses_to_file()
        self.show_main_menu()

    def save_expenses_to_file(self, filename="expenses.txt"):
        with open(filename, "w") as file:
            for category, budget_instance in project10.budget_category.items():
                file.write(f"{category}\n")
                for expense_type, cost in budget_instance.expenses_dict.items():
                    file.write(f"{expense_type}: ${cost}\n")

                file.write("\n")

    def show_all_expenses(self):
        self.clear_screen()

        self.title_label = Label(self.menu, 
                                 text="All Expenses", 
                                 font=("Arial", 30, "bold"), 
                                 fg="#ADD8E6")
        self.title_label.pack(pady=10)

        self.current_widgets = [self.title_label]

        if not project10.budget_category:
            no_expense_label = Label(self.menu, 
                                     text="No expenses recorded yet.", 
                                     font=("Arial", 20))
            no_expense_label.pack()
            
            self.current_widgets.append(no_expense_label)
            return

        # Iterate through all categories
        for category_name, budget_instance in project10.budget_category.items():
            category_label = Label(self.menu, 
                                   text=f"Category: {category_name}", 
                                   font=("Arial", 20, "bold"), 
                                   fg="green")
            category_label.pack(pady=5)
            
            self.current_widgets.append(category_label)

            if not budget_instance.expenses_dict:
                empty_label = Label(self.menu, 
                                    text="No expenses yet.", 
                                    font=("Arial", 16),
                                    fg="green"
                                    )
                empty_label.pack()
                self.current_widgets.append(empty_label)
            
            else:
                for expense_type, cost in budget_instance.expenses_dict.items():
                    expense_label = Label(self.menu, 
                                          text=f"{expense_type}: ${cost}", font=("Arial", 16))
                    expense_label.pack()
                    self.current_widgets.append(expense_label)

        # Back button
        back_btn = Button(self.menu, 
                          text="Back to Menu", 
                          width=25, 
                          height=3, 
                          command=self.show_main_menu)
        back_btn.pack(pady=10)
        self.current_widgets.append(back_btn)

    def collect_financial_status(self):
        self.clear_screen()

        self.collect_income_label = Label(menu,
                                          text="What is your income",
                                          font=("Arial", 20))
        self.collect_income_label.pack()

        self.collect_income = Entry(menu)
        self.collect_income.pack()

        self.submit_income = Button(menu,
                                    text="Submit",
                                    width=25,
                                    height=3,
                                    command=self.view_financial_status)
        self.submit_income.pack()

        self.current_widgets = [self.collect_income_label, self.collect_income, self.submit_income]

    def view_financial_status(self):
        self.clear_screen()

        self.balance = Budget.calc_total_balance(int(self.collect_income.get()))

        if self.balance > 0:
            self.finiancial_status = Label(menu, 
                                           text=f"Great! You are saving money!", 
                                           font=("Arial", 20, "bold"), 
                                           fg="#000080")
            self.finiancial_status.pack()

            self.balance = Label(menu,
                                        text=f"Your balance is {self.balance}",
                                        font=("Arial",15))
            self.balance.pack()

        elif self.balance == 0:
            self.finiancial_status = Label(menu, 
                                           text=f"You are breaking even!", 
                                           font=("Arial", 20, "bold"), 
                                           fg="#808080")
            self.finiancial_status.pack()

            self.balance_display = Label(menu,
                                        text=f"Your balance is {self.balance}",
                                        font=("Arial",15))
            self.balance_display.pack()

        else:
            self.finiancial_status = Label(menu, 
                                           text=f"**WARNING** You are overspending!", 
                                           font=("Arial", 20, "bold"), 
                                           fg="#FF0000")
            self.finiancial_status.pack()

            self.balance_display = Label(menu,
                                        text=f"Your balance is {self.balance}",
                                        font=("Arial",15))
            self.balance_display.pack()

        self.back_btn = Button(menu,
                               text="Return to Menu",
                               width=25,
                               height=5,
                               command=self.show_main_menu)
        self.back_btn.pack()

        self.current_widgets = [self.finiancial_status, self.balance_display, self.back_btn]

if __name__ == "__main__":
    menu = Tk()
    menu.configure(bg="purple") 
    app = BudgetBuddyApp(menu)
    menu.mainloop()
