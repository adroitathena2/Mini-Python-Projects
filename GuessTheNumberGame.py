import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")
        self.master.geometry("300x220")
        self.master.configure(bg="#c3dae3")
        self.master.minsize(300, 220)  # Set a minimum window size

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        # Main label
        self.label = tk.Label(master, text="Enter your guess (1-100):", font=("Helvetica", 16, "bold"), bg="#c3dae3", wraplength=280)
        self.label.pack(pady=10)

        # Guess entry
        self.guess_entry = tk.Entry(master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=5)

        # Attempts label
        self.attempts_label = tk.Label(master, text="10 attempts only", font=("Helvetica", 10), bg="#c3dae3")
        self.attempts_label.pack()

        # Guess button
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white")
        self.guess_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#c3dae3", wraplength=280)
        self.result_label.pack(pady=10)

    def check_guess(self):
        guess = self.guess_entry.get()
        
        if not guess.isdigit():
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.", fg="red")
            if self.number_to_guess - guess <= 5:
                self.result_label.config(text="You're close! Too low! Try again.", fg="orange")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.", fg="red")
            if guess - self.number_to_guess <= 5:
                self.result_label.config(text="You're close! Too high! Try again.", fg="orange")
        else:
            self.result_label.config(text=f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts.", fg="green")
            self.guess_button.config(state=tk.DISABLED)
            return

        if self.attempts >= self.max_attempts:
            self.result_label.config(text=f"Sorry! You've used all {self.max_attempts} attempts. The number was {self.number_to_guess}.", fg="red")
            self.guess_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
