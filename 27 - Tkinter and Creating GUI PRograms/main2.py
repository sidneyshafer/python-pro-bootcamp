# **An element with NO Pack(), Place(), or Grid() will not be shown**
# Pack() - starts at top of screen and places each element below
# -- Can change "side" parameter to left, bottom, or right
# Place() - precise positioning
# -- Can provide an (x, y) value
# -- downside: very specific
# Grid() - images entire program is a grid
# -- can divide it into as many rows/columns as you can
# -- rows go horizontal, columns go vertical
# -- best/easiest way to layout elements
# -- CANNOT MIX GRID AND PACK

from tkinter import *


def btn_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)
    print(new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
# ADD PADDING
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
# ADD PADDING
my_label.config(padx=10, pady=10)

# Both do the same thing
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button1 = Button(text="Click Me", command=btn_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entries
user_input = Entry(width=10)
# Gets text in entry
print(user_input.get())
user_input.grid(column=3, row=2)


window.mainloop()
