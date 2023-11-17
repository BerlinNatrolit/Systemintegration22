# Application for button and label.

from tkinter import *

def clicked():
    label.configure(text="I just got clicked and i am awesome")

root = Tk()
root.title("Hello world!")
root.geometry("500x400")

label = Label(root, text="Hello World!")
label.grid()

button = Button(root, text = "Click me", fg="red", command = clicked)
button.grid(column=1, row=0)

root.mainloop()



