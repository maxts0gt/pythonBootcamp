from random import choice, randint, shuffle
from tkinter import *
import pandas as pd
from pandas.io.parsers import read_csv
import random
TITLE = ("Ariel", 40, "italic")
TEXT = ("Ariel", 60, "bold")
BLACK = "#000"
BACKGROUND_COLOR = "#B1DDC6"

# --------------------------READ DATA FROM CSV----------------------------------------#
data = pd.read_csv("data/french_words.csv")
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    original_data = pd.read_csv("data/french_words.read_csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------CLICK BUTTON ACTION----------------------------------------#


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images\card_back.png")
front_image = PhotoImage(file="images\card_front.png")
card_background = canvas.create_image(400, 263, image=front_image)

# Setting up Right Button
card_title = canvas.create_text(400, 150, text="", font=TITLE)
card_word = canvas.create_text(400, 263, text="", font=TEXT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Setting up Wrong Button
unknown = PhotoImage(file="images\wrong.png")
unknown_button = Button(image=unknown, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known = PhotoImage(file="images\correct.png")
known_button = Button(image=known, highlightthickness=0,
                      command=is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()
