from datetime import date
from dateutil.parser import parse
from PIL import Image
from typing import Tuple

# TODO: scale square pics based on the number of weeks
# TODO: merge functionality for calculating days, weeks (and, maybe, months and years)
# TODO: do more precise calculations by being specific (e.g., ask gender and location of birth)


# Generating a calendar for days is less practical than weeks
# I'm leaving this stuff in until I refactor it into a more generic function/class
def calculate_days(*dob: int) -> int:
    """
        Calculate the number of days left to live based on date of birth
        NOTE: This function was a mistake, but just in case you want to know the number of days I'm leaving it in
    """
    average_life_expectancy = 26097.5         # based on the average human life expectancy (~71.5 yrs)

    days_lived = abs(date.today() - date(*dob)).days
    days_left = average_life_expectancy - days_lived

    return days_left


# Actually relevant code starts here
def input_dob() -> Tuple[int, int, int]:
    dob = input('Enter your date of birth (YYYY-MM-DD):\n')
    dob = parse(dob)
    return dob.year, dob.month, dob.day


def calculate_weeks(*dob: int) -> int:
    """
        Calculate the number of weeks left to live based on date of birth
    """
    average_life_expectancy = 3728.214        # based on the average human life expectancy (~71.5 yrs)

    weeks_lived = abs(date.today() - date(*dob)).days / 7
    weeks_left = average_life_expectancy - weeks_lived

    return int(weeks_left)


def generate_calendar(weeks: int):
    """
        Generate a calendar based on the number of weeks
    """
    square_path = 'img/square.jpg'
    background_path = 'img/background.png'

    square_size = (50, 50)
    cols = 48
    padding = 40
    rows, leftover = divmod(weeks / cols, 1)
    rows = int(rows) + 1

    with Image.open(square_path) as square, Image.open(background_path) as background:
        print(background.format, background.size, background.mode)
        print(square.format, square.size)
        square = square.resize(square_size)

        for row in range(0, rows):
            if row == rows - 1 and leftover != 0:
                cols *= leftover
                cols = int(cols)
            for col in range(0, cols):
                box = (square.size[0] * col + padding, square_size[1] * row + padding)
                background.paste(square, box)

        background.show()


if __name__ == '__main__':
    weeks = calculate_weeks(*input_dob())
    generate_calendar(weeks)
