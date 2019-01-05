# Scraper of the The World Bank's most recent life expectancy stats
# All the scraped life expectancy data belongs to The World Bank Group (http://www.worldbank.org/)
# The code belongs to me, kronicka (https://github.com/kronicka)

from bs4 import BeautifulSoup
from pycountry import countries
import requests
import json


def scrape_life_expectancy(country: str) -> int:
    """
    Scrape life expectancy by country from World Bank's most recent data.

    Params:
        country (str): country's 3-letter alias (e.g., "Afghanistan" = "AFG")

    Returns:
        life_expectancy_years (int): number of years of projected life expectancy in the specified country

    """
    widget_url = 'https://databank.worldbank.org/data/views/reports/reportwidget.aspx'
    report_url = f'?Report_Name=CountryProfile&Id=b450fd57&tbar=y&dd=y&inf=n&zm=n&country={country}'
    data_url = widget_url + report_url
    onclick_value = "loadMetaData('SP.DYN.LE00.IN','S','Series','Life expectancy at birth, total (years)','2','1801')"
    life_expectancy_years = None

    try:
        response = requests.get(data_url)
        life_expectancy_years = BeautifulSoup(response.text, 'html.parser') \
                                                .find(attrs={'onclick': onclick_value}) \
                                                .parent \
                                                .find_all('td')[-1] \
                                                .find('div').get_text()
        if life_expectancy_years == '..':
            life_expectancy_years = 0
    except requests.exceptions.ConnectionError:
        print('Couldn\'t reach the World Bank server, pal, fix your connection for the most recent data.')
        print('Using locally stored 2016 data for countries instead.')

        with open('countries.txt', 'r') as countries_file:
            countries_dict = json.loads(countries_file.read())
            life_expectancy_years = countries_dict[country]
            print(f'Fetched {country}: {life_expectancy_years}')
    except requests.exceptions.RequestException as e:
        print(e)

    return int(life_expectancy_years)


def store_scraped_data_in_file():
    """
    Evoke this function to manually store the scraped data locally, for cases when there's no Internet connection.
    Takes hella lot of time.
    The dict with key-value (country-life_expectancy) pairs will be stored in countries.txt

    """
    countries_local = {}
    country_codes = [country.alpha_3 for country in countries]

    for country in country_codes:
        expectancy = scrape_life_expectancy(country)
        countries_local[country] = expectancy
        print(f'Fetched {country}: {expectancy}')

    with open('countries.txt', 'w') as countries_file:
        countries_file.write(json.dumps(countries_local))


if __name__ == '__main__':
    print('Running the scraper and storing data as a serialized dict for all countries in /countries.txt.')
    store_scraped_data_in_file()
