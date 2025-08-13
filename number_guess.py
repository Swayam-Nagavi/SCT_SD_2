import tkinter as tk
import random

number_to_guess = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number_to_guess:
            result_label.config(text="📉 Too low! Try again.", fg="blue")
        elif guess > number_to_guess:
            result_label.config(text="📈 Too high! Try again.", fg="orange")
        else:
            result_label.config(text=f"🎉 Correct! The number was {number_to_guess}.", fg="green")
            guess_button.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="❌ Please enter a valid number.", fg="red")

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    entry.delete(0, tk.END)
    result_label.config(text="", fg="black")
    guess_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Guess the Number 🎯")
root.geometry("400x400")
root.config(bg="#121212")

title_label = tk.Label(root, text="Guess the Number!", font=("Arial", 18, "bold"), bg="#121212", fg="white")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Check Guess", font=("Arial", 12, "bold"), bg="#00ffcc", fg="black", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#121212", fg="white")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="🔄 Play Again", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()