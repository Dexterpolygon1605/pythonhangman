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