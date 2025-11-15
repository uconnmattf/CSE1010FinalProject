
from tkinter import *
from PIL import Image, ImageTk

def main():
    def addexpense():
        print("test")

    selection_menu = Toplevel()
    selection_menu.geometry("700x600")

    add_expense_button = Button(selection_menu,
                                text="Add Expenses",
                                command=addexpense)
    add_expense_button.pack()

    # Using Pillow cuz tkinter is buns
    img1 = Image.open("Images/jtempimage2.png").resize((200, 200))
    img2 = Image.open("Images/jtempimage1.png").resize((250, 250))
    selection_menu.temp_image1 = ImageTk.PhotoImage(img1)
    selection_menu.temp_image2 = ImageTk.PhotoImage(img2)

    adding_expenses = Label(selection_menu,
                            text="This bum ass jobless nigga griefed all my games",
                            font=("Arial", 20, "bold"),
                            image=selection_menu.temp_image1,
                            compound="bottom")
    adding_expenses.pack()

    temp_label = Label(selection_menu,
                       image=selection_menu.temp_image2)
    temp_label.pack()

if __name__ == "__main__":
    main()