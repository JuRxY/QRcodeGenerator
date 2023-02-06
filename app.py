from tkinter import *
from create_code import make_code

root = Tk()
root.title("QR code generator")


name_label = Label(root, text="Name of file: ", font=120)
name_label.grid(row=0, column=0)

name_entry = Entry(root, bd=1, font=("Arial black", 15))
name_entry.grid(row=0, column=1)

content_label = Label(root, text="Content/url: ", font=120)
content_label.grid(row=3, column=0)

content_entry = Entry(root, bd=1, font=("Arial black", 15))
content_entry.grid(row=3, column=1)

def get_text():
    name = name_entry.get()
    content = content_entry.get()
    make_code(content, name)
    quit()

confirm_button = Button(root, text="Generate", font=120, command=get_text)
confirm_button.grid(row=4, column=1)

root.mainloop()