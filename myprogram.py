# guess_number.py

import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    tries = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            tries += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {tries} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
