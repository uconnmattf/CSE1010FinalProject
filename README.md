import tkinter as tk
import project10
import selectionmenu
from PIL import Image, ImageTk


print(f"using this file {project10.__file__}")


def submit():
    selectionmenu.main()
    main_menu.withdraw()


main_menu = tk.Tk()
main_menu.geometry("420x420")
main_menu.title("Budget Buddy")


banner_img = Image.open("CSE1010FinalProject/Images/money_bannerfrontpage.png")
banner_photo = ImageTk.PhotoImage(banner_img)


icon_img = Image.open("CSE1010FinalProject/Images/Budget_Icon.png")
icon_img = icon_img.resize((icon_img.width // 2, icon_img.height // 2), Image.LANCZOS)
icon_photo = ImageTk.PhotoImage(icon_img)

main_menu.iconphoto(True, icon_photo)  



title = tk.Label(
    main_menu,
    text="Budget Buddy",
    font=("Arial", 40, "bold"),
    fg="#ADD8E6",
    relief=tk.RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=banner_photo,   # ← FIXED: uses PIL PhotoImage
    compound="top"
)
title.pack()
title.image = banner_photo  



name_label = tk.Label(
    main_menu,
    text="Enter your name.",
    font=("Arial", 20, "bold")
)
name_label.pack()



name_box = tk.Entry(main_menu)
name_box.pack()



submit_button = tk.Button(
    main_menu,
    text="Submit",
    command=submit
)
submit_button.pack()


main_menu.mainloop()
