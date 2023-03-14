# This program converts miles to kilometers
from tkinter import *


def calc():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilo_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to:")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(column=1, row=2)


window.mainloop()
