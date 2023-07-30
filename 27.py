# Advanced Functions. Default Arguments, *Args, **Kwargs
'''
Unlimited Arguments
def add(*args):
    for n in args:
        print(n)

**kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)
'''

# class Car:
#
#     def __init__(self, **kw):
#         # self.make = kw['make']
#         # self.mdoel = kw['model']
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="nissan", model="GT-R")
# print(my_car.model)

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

'''
layout manager 1) pack, 2) place, 3) grid
'''
#Label
my_label = Label(text="I Am a Label", font=("Arial",24,"bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "new text"
my_label.config(text="NEW TEXT")

#Button

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Net Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
# print(input.get())

window.mainloop()