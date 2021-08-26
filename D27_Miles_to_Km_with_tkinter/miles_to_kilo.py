from tkinter import *
FONT = ("Ariel", 12)


def button_clicked():
    answer = float(entry.get())
    km = answer * 1.609
    miles_label3.config(text=f"{km}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=120)
window.config(padx=30, pady=30)


entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_label1 = Label(text="Miles", font=FONT)
miles_label1.grid(column=2, row=0)

miles_label2 = Label(text="is equal to", font=FONT)
miles_label2.grid(column=0, row=1)

miles_label3 = Label(text="", font=FONT)
miles_label3.grid(column=1, row=1)

# my_label.config(text="I got clicked")

miles_label4 = Label(text="Km", font=FONT)
miles_label4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
