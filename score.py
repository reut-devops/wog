import utils


def add_score(difficulty):
    try:
        with open(utils.SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError as ex:
        current_score = 0
        utils.BAD_RETURN_CODE = ex
    except ValueError as e:
        print("Set current_score = 0 , Error:", e)
        utils.BAD_RETURN_CODE = e
        current_score = 0

    current_score += (difficulty * 3) + 5

    with open(utils.SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))


def get_score():
    with open(utils.SCORES_FILE_NAME, 'r') as file:
        return int(file.read())
