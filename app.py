# All the scraped life expectancy data belongs to The World Bank Group (http://www.worldbank.org/)
# The code is written by me, kronicka (https://github.com/kronicka) and is licensed under GNU 3.0

import constants
from datetime import date
from dateutil.parser import parse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pycountry import countries
from typing import Tuple
from scraper import scrape_life_expectancy

# TODO: merge functionality for calculating days, weeks (and, maybe, months and years)
# TODO: let the user pick a shape
# TODO: separate methods into one class
# TODO: add SVG support


# Validators
valid_f_sex = ['female', 'f', 'F', 'fem', 'she', 'woman']
valid_m_sex = ['male', 'm', 'M', 'man', 'he']


def input_dob() -> Tuple[int, int, int]:
    """
    Input and validate date of birth
    """
    dob = input('Enter your date of birth (YYYY-MM-DD):\n')
    dob = parse(dob)
    return dob.year, dob.month, dob.day


def input_sex() -> bool:
    """
    Input and validate biological sex
    """
    while True:
        sex = input('Enter your biological sex (m/f):\n')
        if sex in valid_f_sex:
            return True
        elif sex in valid_m_sex:
            return False
        else:
            print('Please enter a valid biological sex.')


def input_country() -> str:
    """
    Input a valid country or a 2-letter country alias (e.g., "Germany" = "DE")
    """
    while True:
        country = input('Enter your country (full name or 2-letter alias):\n')
        country_names = [country.name for country in countries]
        country_codes = [country.alpha_2 for country in countries]

        if country.capitalize() in country_names:
            return countries.get(name=country.capitalize()).alpha_3
        elif country.upper() in country_codes:
            return countries.get(alpha_2=country.upper()).alpha_3
        else:
            print('Please enter a valid country name.')


def input_all():
    """
    Input all the needed arguments for the calendar.
    """
    dob = input_dob()
    sex = input_sex()
    country = input_country()
    country_index = scrape_life_expectancy(country)

    return sex, country_index, dob


def draw_text(img: Image) -> None:
    """
    Draw a tagline on the bottom of the generated image.
    """
    text = 'This is your life on a single sheet of paper.'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    padding_left = 226        # The almost exact estimated half of pixel width of the current default tagline
    padding_bottom = 40
    draw.text(((img.size[0] / 2) - padding_left, img.size[1] - padding_bottom), text, (192, 192, 192), font=font)
    # img.save('weeks.png')


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


def generate_calendar(units: int, unit_type: str = None):
    """
    Generate a calendar based on the number of weeks
    """
    square_path = 'img/square.jpg'
    background_path = 'img/background.png'

    square_size = (50, 50)
    cols = 48
    padding = 40

    if unit_type == 'days':
        square_size = (10, 10)
        cols = 240
        padding = 40

    rows, leftover = divmod(units / cols, 1)
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

        draw_text(background)
        # background.save('weeks.png')
        background.show()


if __name__ == '__main__':
    inputs = input_all()
    weeks = calculate_weeks(*inputs)
    generate_calendar(weeks)


