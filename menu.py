from tkinter import *
import project10
from PIL import Image, ImageTk

#IMPORT PILLOW BEFORE RUNNING CUZ TKINTER IS ASS AND CANT READ SOME IMAGES
#DO pip install Pillow OR NOTHING WILL WORK PROBABLY IDK


print(f"using this file{project10.__file__}")


def submit_name():
    #project10.main(name_box.get()) <--- Runs the main code from project10.py/commented out for testing speed reasons
    adding_expenses = Label(menu,
                            text=f"Hello {name_box.get()}, this is BudgetBuddy! Your personal Budgeting Assistant.",
                            font=("Arial", 20, "bold"),
                            fg="#ADD8E6",
                            relief=RAISED,
                            bd=10,
                            padx=20,
                            pady=20, 
                            compound="top")
    adding_expenses.pack()
    
    text_label1 = Label(menu,
                        text="What would you like to do?",
                        font=("Arial", 20, "bold"),
                        )
    text_label1.pack()

    new_expense_category = Button(menu,
                         text="Create a new expense category",
                         width=25,
                         height=5)
    new_expense_category.pack()

    add_expenses = Button(menu,
                         text="Add expenses into a category",
                         width=25,
                         height=5)
    add_expenses.pack()

    display_expenses = Button(menu,
                              text="Display expenses",
                              width=25,
                              height=5)
    display_expenses.pack()

    financial_status = Button(menu,
                              text="View financial status",
                              width=25,
                              height=5)
    financial_status.pack()

    save_expense = Button(menu,
                              text="View financial status",
                              width=25,
                              height=5)
    save_expense.pack()


    #hides all the labels that were orginally present so we don't need to make new windows repeatdly
    title.pack_forget()
    name_label.pack_forget()
    name_box.pack_forget()
    submit_button.pack_forget()



menu = Tk()


menu.geometry("1024x768")
menu.title("Budget Buddy")

img1 = Image.open("Images/jtempimage2.png").resize((200, 200))
img2 = Image.open("Images/jtempimage1.png").resize((250, 250))
menu.temp_image1 = ImageTk.PhotoImage(img1)
menu.temp_image2 = ImageTk.PhotoImage(img2)



title_photo = PhotoImage(file="Images\Budget_Icon.png")
smaller_title_photo = title_photo.subsample(2, 2) #reduces size of the image
menu.iconphoto(True, title_photo)

title = Label(menu, 
              text="Budget Buddy", 
              font=("Arial",40,"bold"), 
              fg="#ADD8E6",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20, 
              compound="top")
title.pack()

name_label = Label(menu,
                   text="Enter your name.",
                   font=("Arial",20,"bold"))
name_label.pack()


name_box = Entry(menu)
name_box.pack()

submit_button = Button(menu,
                       text="Submit",
                       command=submit_name)
submit_button.pack()

#Gui Elements after the name input screen







menu.mainloop()
