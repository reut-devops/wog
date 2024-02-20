import random
import time

from utils import validate_input


def generate_sequence(difficulty):
    generate_list = []
    for i in range(0, difficulty):
        generate_list.insert(i, random.randrange(1, 101))
    return generate_list


def get_list_from_user(difficulty):
    print("Please recall and input the displayed numbers ")
    user_list = []
    for i in range(0, difficulty):
        user_list.insert(i, validate_input(input(f"Enter number :  "), 1, 101))
    return user_list


def compare_results(generate_list, user_list, difficulty):
    for i in range(1, difficulty):
        if generate_list[i] != user_list[i]:
            return False
    return True


def play(difficulty):
    print("Start Guess Game")
    generate_list = generate_sequence(difficulty)

    for number in generate_list:
        print(number, end=' ', flush=True)
        time.sleep(1)

    time.sleep(3)
    print("\033[A                             \033[A")

    user_list = get_list_from_user(difficulty)
    return compare_results(generate_list, user_list, difficulty)
