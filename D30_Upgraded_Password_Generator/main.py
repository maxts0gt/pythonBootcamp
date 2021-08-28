from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
WHITE = "#fff"
BLACK = "#000"
FONT = ("Times New Roman", 15)

# ---------------------------- Searches through JSON Data Shows the Result in a Pop-Up


def search():
    # Reading old data

    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Not Found",
                            message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found",
                                message=f"No details for {website} found.")

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
    password_entry.insert(0, passwords)
    pyperclip.copy(passwords)
# --------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# 0. TODO UI Creation
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=220, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(70, 100, image=lock_img)
canvas.grid(column=1, row=0, columnspan=2)

# 1. TODO Label
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# 2. TODO Entries
website_entry = Entry(width=21, highlightthickness=1)
website_entry.grid(row=1, column=1, sticky="W")
website_entry.focus()

email_entry = Entry(width=45, highlightthickness=1)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "max@maxtsogt.com")

password_entry = Entry(width=21, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky="W")


# 3. TODO Button

generator = Button(text="Search", command=search, width=15)
generator.grid(row=1, column=2)

generator = Button(text="Generate Password", command=generate_password)
generator.grid(row=3, column=2)

generator = Button(text="Add", command=add_clicked, width=38)
generator.grid(row=4, column=1, columnspan=2)


window.mainloop()
