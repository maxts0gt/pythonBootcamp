from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
WHITE = "#fff"
BLACK = "#000"
FONT = ("Times New Roman", 15)

# ---------------------------- PASSWORD GENERATOR #Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for letter in range(randint(2, 4))]
    password_numbers = [choice(numbers) for letter in range(randint(2, 4))]

    password_list = (password_letters + password_symbols + password_numbers)
    shuffle(password_list)

    passwords = "".join(password_list)
    password.insert(0, passwords)
    pyperclip.copy(passwords)
# --------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():

    website_data = website.get()
    email_data = email.get()
    password_data = password.get()
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email_data}\nPassword: {password_data}\nIs it okay to save?")
        if is_ok == True:
            with open("pass_data.txt", "a") as file:
                file.write(
                    f"{website_data} | {email_data} | {password_data}\n")
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# 0. TODO UI Creation
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=220, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(70, 100, image=lock_img)
canvas.grid(column=1, row=0, columnspan=2)

# 1. TODO Entries
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# 2. TODO Entries
website = Entry(width=45, highlightthickness=1)
website.grid(row=1, column=1, columnspan=2, sticky="W")
website.focus()

email = Entry(width=45, highlightthickness=1)
email.grid(row=2, column=1, columnspan=2, sticky="W")
email.insert(0, "max@maxtsogt.com")

password = Entry(width=21, highlightthickness=1)
password.grid(row=3, column=1, sticky="W")


# 3. TODO Entries
generator = Button(text="Generate Password", command=generate_password)
generator.grid(row=3, column=2)

generator = Button(text="Add", command=add_clicked, width=38)
generator.grid(row=4, column=1, columnspan=2)


window.mainloop()
