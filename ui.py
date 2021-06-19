from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
import html
from question_model import Question

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x650")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(self.window, text="Score: {}/{}".format(self.quiz.score, len(self.quiz.question_list)),
                                 bg=THEME_COLOR, fg="white", font=20)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=350)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=10)

        check_img = PhotoImage(file="true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.true_answer)
        self.check_button.grid(row=2, column=0, padx=20, pady=20)

        cross_img = PhotoImage(file="false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.false_answer)
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)

        self.question_text = self.canvas.create_text(150, 150, text="Quiz Start", width=200,
                                                     font=("Arial", 20, "italic"))

        self.get_next_question()

        self.stop = 0
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            # print(self.quiz.question_number)
        except IndexError:
            self.stop = 1

    def true_answer(self):
        if self.stop == 0:
            self.isright = self.quiz.check_answer("True")
            # print(self.isright)
            if self.isright:
                self.score_label.config(text="Score: {}/{}".format(self.quiz.score, len(self.quiz.question_list)))

            self.give_feedback()
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended")

    def false_answer(self):
        if self.stop == 0:
            self.isright = self.quiz.check_answer("False")
            # print(self.isright)
            if self.isright:
                self.score_label.config(text="Score: {}/{}".format(self.quiz.score, len(self.quiz.question_list)))
            self.give_feedback()
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended")

    def give_feedback(self):
        if self.isright:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000,self.get_next_question)

