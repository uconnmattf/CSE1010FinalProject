from tkinter import *
import project10

def click():
    project10.main()


window = Tk()

window.geometry("420x420")
window.title("Budget Buddy")

title_photo = PhotoImage(file="Images\Budget_Icon.png")
smaller_title_photo = title_photo.subsample(2, 2) #reduces size of the image
window.iconphoto(True, title_photo)

title = Label(window, 
              text="Budget Buddy", 
              font=("Arial",40,"bold"), 
              fg="#ADD8E6",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20, 
              image = smaller_title_photo,
              compound="top")
title.pack()

start_button = Button(window,
                      text="Start",
                      command=click)
start_button.pack()

window.mainloop()
