# All the scraped life expectancy data belongs to The World Bank Group (http://www.worldbank.org/)
# The code is written by me, kronicka (https://github.com/kronicka), and is licensed under GNU 3.0

from utils import constants
from datetime import date
from PIL import Image
from typing import Tuple
from utils.input import input_all
from utils.draw import draw_text, draw_units_number


# TODO: merge functionality for calculating days, weeks (and, maybe, months and years)
# TODO: let the user pick a shape
# TODO: separate methods into one class
# TODO: add SVG support


def calculate_weeks(sex: bool, country_index: int, dob: Tuple[int, int, int]) -> int:
    """
    Calculate the number of weeks left to live based on date of birth

    Params:
        sex (bool): biological sex, False for male, True for female
        country_index (int): number of years of life expectancy by country
        dob (Tuple[int, int, int]): year, month, day of birth, in that order

    Returns:
        weeks_left (int): projected number of weeks left to live

    """
    country_life_expectancy_weeks = country_index * 365 / 7 if country_index and country_index != 0 else None
    sex_life_expectancy_weeks = constants.female_life_expectancy_weeks if sex else constants.male_life_expectancy_weeks

    if country_life_expectancy_weeks:
        weeks_predicted = (country_life_expectancy_weeks + sex_life_expectancy_weeks) / 2
    else:
        weeks_predicted = sex_life_expectancy_weeks

    weeks_lived = abs(date.today() - date(*dob)).days / 7
    weeks_left = weeks_predicted - weeks_lived
    print(weeks_left)

    return int(weeks_left)


def generate_calendar(units: int, unit_type: str = 'weeks'):
    """
    Generate a calendar based on the number of weeks
    """
    square_size = (50, 50)
    cols = 48
    padding = 40

    if unit_type == 'days':
        square_size = (10, 10)
        cols = 240
        padding = 40

    rows, leftover = divmod(units / cols, 1)
    rows = int(rows) + 1

    with Image.open(constants.square_path) as square, Image.open(constants.background_path) as background:
        print(background.format, background.size, background.mode)
        print(square.format, square.size)
        square = square.resize(square_size)

        for row in range(0, rows):
            if row == rows - 1 and leftover != 0:
                cols *= leftover
                cols = int(cols)
            for col in range(0, cols):
                box = (square.size[0] * col + padding, square_size[1] * row + padding * 2)
                background.paste(square, box)

        draw_text(background)
        draw_units_number(background, units, unit_type)
        background.save('weeks.png')
        background.show()


if __name__ == '__main__':
    inputs = input_all()
    weeks = calculate_weeks(*inputs)
    generate_calendar(weeks)

