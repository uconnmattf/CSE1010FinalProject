from tkinter import *
from PIL import Image, ImageTk

class BudgetBuddyApp:
    def __init__(self, menu):
        self.menu = menu
        self.menu.geometry("1024x768")
        self.menu.title("Budget Buddy")

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
        
        self.btn_add_expenses = Button(self.menu, 
                                       text="Add expenses into a category", 
                                       width=25, 
                                       height=3)
        
        self.btn_display_expenses = Button(self.menu, 
                                           text="Display expenses", 
                                           width=25, 
                                           height=3)
        
        self.btn_financial_status = Button(self.menu, 
                                           text="View financial status", 
                                           width=25, 
                                           height=3)
        
        self.btn_save_expense = Button(self.menu, 
                                       text="Save expenses", 
                                       width=25, 
                                       height=3)

        for btn in [self.btn_new_category, self.btn_add_expenses, self.btn_display_expenses, 
                    self.btn_financial_status, self.btn_save_expense]:
            btn.pack(pady=5)

        self.current_widgets = [self.greeting, self.prompt, self.btn_new_category, 
                                self.btn_add_expenses, self.btn_display_expenses, 
                                self.btn_financial_status, self.btn_save_expense]

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


if __name__ == "__main__":
    menu = Tk()
    app = BudgetBuddyApp(menu)
    menu.mainloop()
