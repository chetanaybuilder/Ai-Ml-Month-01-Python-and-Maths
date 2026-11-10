# Import the standard-library module used to generate the secret number.
import random

# global scope.
MAX_ATTEMPTS = 5

# Welcome the player and explain the game rules.
def greet_user():
    print("+----------------------------------------+")
    print("|          NUMBER GUESSING GAME          |")
    print("+----------------------------------------+")
    player_name = input("Hello! What is your name? ")
    print(
        f"Welcome, {player_name}! You have "
        f"{MAX_ATTEMPTS} attempts to guess the number."
    )

# Run one round of the number-guessing game.
def play_game():
    secret_no = random.randint(1,100)
    attempts_left = MAX_ATTEMPTS
    history = []

    # Compare each guess with the secret number and provide feedback.
    while attempts_left > 0:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        history.append(guess)
        if guess == secret_no:
            print(f"Congratulations! You guessed {secret_no} correctly!")
        elif guess < secret_no:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")

        attempts_left -= 1
        print(f"Attempts remaining: {attempts_left}")

# Reveal the secret number after the available attempts are used.
    print(f"Game over. The secret number was {secret_no}.")

if __name__ == "__main__":
    greet_user()
    play_game()