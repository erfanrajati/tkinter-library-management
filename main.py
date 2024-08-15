from tkinter import *
import backend

lib = backend.Library()

root = Tk()
root.geometry("500x600")

nameIn = Entry(root)
yearIn = Entry(root)
authorIn = Entry(root)

addbook = Button(
    root, 
    text='Add Book',
    command=lambda: lib.add_book(
        nameIn.get(), 
        int(yearIn.get()), 
        authorIn.get()
    )
)

nameIn.grid(row=0, column=0, padx=7, pady=20)
yearIn.grid(row=0, column=1, padx=7, pady=20)
authorIn.grid(row=0, column=2, padx=7, pady=20)
addbook.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
