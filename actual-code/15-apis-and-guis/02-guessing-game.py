import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.secret_number = random.randint(1,10)

        self.label = tk.Label(root, text="Guess a number between 1 and 10")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.feedback = tk.Label(root, text="")
        self.feedback.pack()

    def check_guess(self):

        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback.config(text=f"you need to give me a number")
            return

        if guess < self.secret_number:
            self.feedback.config(text="You are too low.")
        elif guess > self.secret_number:
            self.feedback.config(text="You are too high.")
        else:
            self.feedback.config(text="You got! Thinking of a new number")
            play_again = messagebox.askyesno(title="Again?", message="Do you want to play again?")
            if play_again:
                self.secret_number = random.randint(1,10)
                self.entry.delete(0, tk.END)
            else:
                root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    game = GuessingGame(root)
    root.mainloop()