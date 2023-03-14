from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# use pandas library to read csv file
# data is now a data frame
data = pandas.read_csv("data/french_words.csv")
# convert data frame to dictionary
to_learn = data.to_dict(orient="records")
current_card = {}


# next card function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# show english word
def flip_card():
    # change text on card to english version
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # change background image
    canvas.itemconfig(card_background, image=card_back_img)


"""
def is_known():
    to_learn.remove(current_card)
    unknown_data = pandas.DataFrame(to_learn)
    unknown_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
"""

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip card using after()
flip_timer = window.after(3000, func=flip_card)

# Canvas image
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# Title text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

# Word text
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))

# Change canvas color
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)

# Create buttons
# unknown button (cross button)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# check mark button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

# call next_card function
next_card()

window.mainloop()
