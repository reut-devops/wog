SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = ''


def validate_input(input_value, min_number, max_number):
    while True:
        input_value = validate_int_input(input_value)
        if min_number <= input_value <= max_number:
            return input_value
        else:
            input_value = input(
                f"Invalid input - Please enter number  within the range of {min_number}- {max_number} ")


def validate_int_input(input_value):
    while True:
        if input_value.isdigit():
            return int(input_value)
        else:
            input_value = input(
                f"Invalid input - enter a number ")


def screen_cleaner():
    print("\033c", end="")
