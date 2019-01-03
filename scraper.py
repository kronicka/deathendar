# Scraper of the The World Bank's most recent life expectancy stats
# All the scraped life expectancy data belongs to The World Bank Group (http://www.worldbank.org/)
# The code belongs to me, kronicka (https://github.com/kronicka)

from bs4 import BeautifulSoup
import requests


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
    except requests.exceptions.ConnectionError:
        print('Couldn\'t reach the World Bank server, pal, fix your connection for the most recent data.')
        print('Using locally stored 2016 data for countries instead.')
    except requests.exceptions.RequestException as e:
        print(e)

    return life_expectancy_years


def store_scraped_data_in_file():
    """
    Evoke this function to manually store the scraped data locally, for cases when there's no Internet connection.
    The dict with key-value (country-life_expectancy) pairs will be stored in countries.txt
    """
    pass