import random
import tkinter as tk
from tkinter import messagebox

# Hangman_stages.py and word_file.py are in the same directory
import Hangman_stages
import word_file

class HangmanGame:
    def __init__(self):
        self.lives = 6
        self.chosen_word = random.choice(word_file.words)
        self.display = ['_' for _ in range(len(self.chosen_word))]
        self.guessed_letters = []
        self.game_over = False

    def guess_letter(self, guessed_letter):
        if guessed_letter in self.guessed_letters:
            return "You've already guessed that letter."

        self.guessed_letters.append(guessed_letter)

        if guessed_letter in self.chosen_word:
            for position in range(len(self.chosen_word)):
                if self.chosen_word[position] == guessed_letter:
                    self.display[position] = guessed_letter
            
        else:
            self.lives -= 1

            if self.lives == 0:
                self.game_over = True
                return f"Incorrect guess. You lose! The word was '{self.chosen_word}'."
            return f"Incorrect guess. You have {self.lives} lives left."

        if '_' not in self.display:
            self.game_over = True
            return "Congratulations! You win!"

        return "Correct guess!" if guessed_letter in self.chosen_word else "Incorrect guess."

    def get_display(self):
        return ' '.join(self.display)

    def get_hangman_stage(self):
        return Hangman_stages.stages[self.lives]


    
def start_game():
    global game
    game = HangmanGame()
    update_display()
    hangman_label.config(text=game.get_hangman_stage())
    guess_entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    

def update_display():
    word_label.config(text=game.get_display())

def make_guess():
    guess = guess_entry.get().lower()
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a single alphabetic character.")
        return

    result = game.guess_letter(guess)
    messagebox.showinfo("Result", result)
    update_display()
    hangman_label.config(text=game.get_hangman_stage())
    if game.game_over:
        guess_button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", result)

# Initialize the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x600")

# Create UI elements with colors
word_label = tk.Label(root, text="", font=("Helvetica", 18), bg="lightblue", fg="black")
word_label.pack(pady=20)

hangman_label = tk.Label(root, text="", font=("Helvetica", 18), bg="lightyellow", fg="black")
hangman_label.pack(pady=20)

guess_entry = tk.Entry(root, font=("Helvetica", 18), bg="white", fg="black")
guess_entry.pack(pady=20)

guess_button = tk.Button(root, text="Guess", command=make_guess, font=("Helvetica", 18), bg="lightgreen", fg="black")
guess_button.pack(pady=20)

start_button = tk.Button(root, text="Start New Game", command=start_game, font=("Helvetica", 18), bg="orange", fg="black")
start_button.pack(pady=20)



# Start the game for the first time
start_game()

# Run the application
root.mainloop()
