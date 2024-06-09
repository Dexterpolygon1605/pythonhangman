import tkinter as tk
import random

word_list = ["python", "hangman", "programming", "challenge"]
secret_word = random.choice(word_list)

correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

def display_game_stats():
    display_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Incorrect Guesses: {' '.join(incorrect_guesses)}")
    print(f"Attempts left: {attempts_left}")

while True:
    display_game_stats()
    guess = input("Guess a letter: ").lower()

    if guess in secret_word:
        correct_guesses.add(guess)

        if set(secret_word).issubset(set(correct_guesses)):
            print("Congratulations! You've guesses the word!")
            break

    else:
        incorrect_guesses.add(guess)
        attempts_left -= 1

        if attempts_left == 0:
            print("You lose!")
            print(f"The secret word was: {secret_word}")
            break


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("HangmanGame")
        self.master.geometry("900x600")
        self.word_list = ["PYTHON", "JAVASCRIPT", "KOTLIN", "JAVA", "RUBY", "SWIFT"]
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

def initialize_gui(self):
    self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
    self.hangman_canvas.pack(pady=20)
    self.word_display = tk.label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30))
    self.word_display.pack(pady=(40, 20))
    self.buttons_frame = tk.Frame(self.master)
    self.buttons_frame.pack(pady=20)
    self.setup_alphabet_button()

def choose_secret_word(self):
        return random.choice(self.word_list)

def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm, self.draw_left_leg, self.draw_right_leg,
                  self.draw_face]
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()

def draw_head(self):
    self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black")

def draw_body(self):
    self.hangman_canvas.create_line(155, 110, 155, 170, fill="black")

def draw_left_arm(self):
    self.hangman_canvas.create_line(155, 130, 125, 150, fill="black")

def draw_right_arm(self):
    self.hangman_canvas.create_line(155, 130, 185, 150, fill="black")

def draw_left_leg(self):
    self.hangman_canvas.create_line(155, 170, 125, 200, fill="black")

def draw_right_leg(self):
    self.hangman_canvas.create_line(155, 170, 185, 200, fill="black")

def draw_face(self):
    self.hangman_canvas.create_line(140, 70, 150, 80, fill="black")
    self.hangman_canvas.create_line(160, 70, 170, 80, fill="black")

    self.hangman_canvas.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")

def guess_letter(self, letter):
    if letter in self.secret_word and letter not in self.correct_guesses:
        self.correct_guesses.add(letter)
    elif letter not in self.incorrect_guesses:
        self.incorrect_guesses.add(letter)
        self.attempts_left -= 1
        self.update_hangman_canvas()

    self.update_word_display()
    self.check_game_over()

def update_word_display(self):
    displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
    self.word.diplay_config(text=displayed_word)

def check_game_over(self):
    if set(self.secret_word).issubset(set(self.correct_guesses)):
        self.diplay_game_over_message("Congratulations! You've guessed the word!")
    elif self.attempts_left == 0:
        self.diplay_game_over_message(f"You lose! The word was:{self.secret_word}")

def setup_alphabet_button(self):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_row = alphabet[:13]
    lower_row = alphabet[13:]

    upper_frame = tk.Frame(self.buttons_frame)
    upper_frame.pack()
    lower_frame = tk.Frame(self.buttons_frame)
    lower_frame.pack()

    for letter in upper_row:
        button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
        button.pack(side="left", padx=2, pady=2)

    for letter in lower_row:
        button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
        button.pack(side="left", padx=2, pady=2)

def display_game_over_message(self, message):
    self.buttons_frame.pack_forget()

    self.game_over_label = tk.Label(self.master, text=message, font=("Helvetica", 18), fg="red")
    self.game_over_label.pack(pady=(10, 20))