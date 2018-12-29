from datetime import date
from dateutil.parser import parse
from PIL import Image
from pycountry import countries
from typing import Tuple

# TODO: scale square pics based on the number of weeks
# TODO: merge functionality for calculating days, weeks (and, maybe, months and years)
# TODO: do more precise calculations by being specific (e.g., ask gender and location of birth)
# TODO: let the user pick a shape
# TODO: separate methods into one class
# TODO: add SVG support


# Validators
valid_f_sex = ['female', 'f', 'F', 'fem', 'she', 'woman']
valid_m_sex = ['male', 'm', 'M', 'man', 'he']

# Constants (2016 UN Data)
general_life_expectancy_days = 26097.5
general_life_expectancy_weeks = 3728.214        # ~71.5 years
female_life_expectancy_weeks = 3872.18071       # ~74.261 years
male_life_expectancy_weeks = 3647.54929         # ~69.953 years


# Generating a calendar for days is less practical than weeks
# I'm leaving this stuff in until I refactor it into a more generic function/class
def calculate_days(*dob: int) -> int:
    """
    Calculate the number of days left to live based on date of birth
    NOTE: This function was a mistake, but just in case you want to know the number of days I'm leaving it in
    """
    days_lived = abs(date.today() - date(*dob)).days
    days_left = general_life_expectancy_days - days_lived

    return days_left


# Actually relevant code starts here
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


def map_country(country: str) -> int:
    """
    Return the average life expectancy based on the country
    """
    pass


def calculate_weeks(sex: bool, country_index: int, *dob: int) -> int:
    """
    Calculate the number of weeks left to live based on date of birth
    """
    weeks_lived = abs(date.today() - date(*dob)).days / 7
    weeks_left = (female_life_expectancy_weeks if sex else male_life_expectancy_weeks) - weeks_lived
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

        background.show()


if __name__ == '__main__':
    # dob = input_dob()
    # sex = input_sex()
    # weeks = calculate_weeks(sex, *dob)
    # days = calculate_days(*dob)
    # generate_calendar(days, 'days')
    c = input_country()
    print(c)

