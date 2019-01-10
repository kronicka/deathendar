from dateutil.parser import parse
from pycountry import countries
from scraper import scrape_life_expectancy
from typing import Tuple


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
