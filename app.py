# All the scraped life expectancy data belongs to The World Bank Group (http://www.worldbank.org/)
# The code is written by me, kronicka (https://github.com/kronicka), and is licensed under GNU 3.0

from utils import constants
from datetime import date
from typing import Tuple
from utils.input import input_all
from utils.calendar import generate_calendar_svg


# TODO: merge functionality for calculating days, weeks (and, maybe, months and years)
# TODO: let the user pick a shape
# TODO: separate methods into one class


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
    sex_life_expectancy_weeks = constants.FEMALE_LIFE_EXPECTANCY_WEEKS if sex else constants.MALE_LIFE_EXPECTANCY_WEEKS

    if country_life_expectancy_weeks:
        weeks_predicted = (country_life_expectancy_weeks + sex_life_expectancy_weeks) / 2
    else:
        weeks_predicted = sex_life_expectancy_weeks

    weeks_lived = abs(date.today() - date(*dob)).days / 7
    weeks_left = weeks_predicted - weeks_lived
    print(weeks_left)

    return int(weeks_left)


if __name__ == '__main__':
    inputs = input_all()
    weeks = calculate_weeks(*inputs)
    generate_calendar_svg(weeks, 'png')

