import math
import random

name = input('Enter your name: ')
print(f"Hi {name},Welcome to the number guessing game\nBefore we start I would like you to type in the range"
      f" of numbers you would like to guess from ")


def calculate_max_guesses(lower, upper):
    range_size = upper - lower + 1  # Including both lower and upper bounds
    max_guesses = math.ceil(math.log2(range_size))  # Calculate max guesses
    return max_guesses


lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

max_attempts = calculate_max_guesses(lower_bound, upper_bound)
print(f"You have a total of {max_attempts} attempts")

number_to_guess = random.randrange(lower_bound, upper_bound + 1)

chances = max_attempts

guess_counter = 0

while guess_counter < chances:
    guess_counter = + 1
    guess = int(input("Enter your Guess: "))
    if guess == number_to_guess and guess_counter <= chances:
        print(f"You guessed right, the number is {number_to_guess}")
        break

    elif guess_counter > chances and guess != number_to_guess:
        print(f"You have exceeded your number of attempts. The number is {number_to_guess}")

    elif guess > number_to_guess:
        print('Your guess is higher ')

    elif guess < number_to_guess:
        print('Your guess is lesser')
