from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="#FFF", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.return_true)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.return_false)
        self.false_button.grid(column=1, row=2, pady=20)
        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="#FFF", font=("Courier", 14), pady=20)
        self.score.grid(column=1, row=0)
        self.label = self.canvas.create_text(150, 125, width=280, text="TEST", font=("Ariel", 16, "italic"), fill=THEME_COLOR)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.label, text=q_text)
        else:
            self.canvas.itemconfig(self.label, text="You've reached to end of it.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def return_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def return_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


