import tkinter as tk
import random

# Function to start a new game
def start_game():
    global secret_number, attempts  # Declare attempts and secret_number as global
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number between 1 and 100")
    attempt_label.config(text="Attempts: 0")
    hint_label.config(text="")
    guess_entry.delete(0, tk.END)

# Function to provide a hint based on the guess
def provide_hint(guess):
    # Calculate the difference between guess and secret_number
    difference = abs(secret_number - guess)
    
    # Provide hints based on proximity
    if difference == 0:
        return "You're right on the money! 🎉"
    elif difference <= 10:
        return "You're getting warm! 🔥"
    elif difference <= 20:
        return "You're warm! Keep going! 🌡️"
    elif difference <= 30:
        return "You're cold, but not frozen! ❄️"
    else:
        return "You're freezing cold! ❄️❄️"

# Function to check the user's guess
def check_guess():
    global attempts  # Declare attempts as global so it can be updated
    try:
        guess = int(guess_entry.get())
        attempts += 1  # Increment the attempts counter
        attempt_label.config(text=f"Attempts: {attempts}")

        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
        
        # Provide proximity-based hint
        hint = provide_hint(guess)
        hint_label.config(text=hint)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game with Hints")

# Create widgets
result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
result_label.pack(pady=10)

guess_label = tk.Label(root, text="Enter your guess:", font=("Arial", 12))
guess_label.pack()

guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", font=("Arial", 12), command=check_guess)
check_button.pack(pady=10)

attempt_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12))
attempt_label.pack(pady=5)

hint_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
hint_label.pack(pady=10)

new_game_button = tk.Button(root, text="New Game", font=("Arial", 12), command=start_game)
new_game_button.pack(pady=10)

# Initialize the game
start_game()

# Run the GUI main loop
root.mainloop()
