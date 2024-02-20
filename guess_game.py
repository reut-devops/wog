import random
from utils import validate_input


def generate_number(difficulty):
    secret_number = random.randrange(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess_number = validate_input(input(f"Please enter number  within the range of 0 - {difficulty}"), 0, difficulty)
    return guess_number


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    print("Start game Guess Game")
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)
