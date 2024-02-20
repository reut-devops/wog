import random
from utils import validate_int_input
from currency_converter import CurrencyConverter


def get_money_interval(difficulty, generated_number):
    converter = CurrencyConverter()
    from_currency = 'USD'
    to_currency = 'ILS'

    converted_amount = converter.convert(generated_number, from_currency, to_currency)
    difference = 10 - difficulty

    return converted_amount - difference, converted_amount + difference


def get_guess_from_user(generated_number):
    guess_number = validate_int_input(input(f"Please enter a guess for the converted value of a {generated_number} $ "))
    return guess_number


def compare_results(difference_min, difference_max, guess):
    return difference_min <= guess <= difference_max


def play(difficulty):
    print("Start Currency Roulette Game")
    generated_number = random.randrange(1, 100)
    difference_min, difference_max = get_money_interval(difficulty, generated_number)
    guess = get_guess_from_user(generated_number)
    return compare_results(difference_min, difference_max, guess)
