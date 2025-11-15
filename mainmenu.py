from tkinter import *
import project10
import selectionmenu

#IMPORT PILLOW BEFORE RUNNING CUZ TKINTER IS ASS AND CANT READ SOME IMAGES
#DO pip install Pillow OR NOTHING WILL WORK PROBABLY IDK


print(f"using this file{project10.__file__}")


def submit():
    #project10.main(name_box.get())
    selectionmenu.main()
    main_menu.withdraw()
    
main_menu = Tk()


main_menu.geometry("420x420")
main_menu.title("Budget Buddy")

title_photo = PhotoImage(file="Images\Budget_Icon.png")
smaller_title_photo = title_photo.subsample(2, 2) #reduces size of the image
main_menu.iconphoto(True, title_photo)

title = Label(main_menu, 
              text="Budget Buddy", 
              font=("Arial",40,"bold"), 
              fg="#ADD8E6",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20, 
              #image = smaller_title_photo,
              compound="top")
title.pack()

name_label = Label(main_menu,
                   text="Enter your name.",
                   font=("Arial",20,"bold"))
name_label.pack()


name_box = Entry(main_menu)
name_box.pack()

submit_button = Button(main_menu,
                       text="Submit",
                       command=submit)
submit_button.pack()



main_menu.mainloop()
