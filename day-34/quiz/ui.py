from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="SCORE: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=1000, height=500)
        background_img = PhotoImage(file="images/background.png")
        self.canvas.create_image(500, 500, image=background_img)
        self.quote_text = self.canvas.create_text(480, 100, width=480, font=("Arial", 26, "bold"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2)
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=3, column=0)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
