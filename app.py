import currency_roulette_game
import guess_game
import memory_game
from utils import validate_input
from score import add_score


def welcome():
    username = input('Please enter your name:')
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    games = {1: {'game_name': 'Memory Game',
                 'description': 'a sequence of numbers will appear for 1 second and you have to guess it back'},
             2: {'game_name': 'Guess Game',
                 'description': 'guess a number and see if you chose like the computer.'},
             3: {'game_name': 'Currency Roulette',
                 'description': 'try and guess the value of a random amount of USD in ILS'}}

    print('Please choose a game to play:')

    for key in games.keys():
        print(f"{key}. {games[key]['game_name']} - {games[key]['description']}")

    game_selected = validate_input(input(), 1, 3)

    print(f'The selected game {game_selected}')

    level_selected = validate_input(input('Please choose level between 1- 5:'), 1, 5)

    print(f'The selected level {level_selected}')

    if game_selected == 1:
        is_win = memory_game.play(level_selected)
        print(f"Memory Game : {is_win}")
    elif game_selected == 2:
        is_win = guess_game.play(level_selected)
        print(f"Guess Game : {is_win}")
    else:
        is_win = currency_roulette_game.play(level_selected)
        print(f"Currency Roulette : {is_win}")

    if is_win:
        add_score(level_selected)
