# Scraper of the The World Bank most recent life expectancy stats
# for when the prediction based on the country is made
from bs4 import BeautifulSoup
import requests


def scrape_life_expectancy(country: str) -> int:
    """
    Scrape life expectancy by country from World Bank's most recent data.
    Params:
        country (str): country's 3-letter alias (e.g., Afghanistan == AFG)
    Returns:
        life_expectancy_years (int): number of years of projected life expectancy in the specified country
    """
    widget_url = 'https://databank.worldbank.org/data/views/reports/reportwidget.aspx'
    report_url = f'?Report_Name=CountryProfile&Id=b450fd57&tbar=y&dd=y&inf=n&zm=n&country={country}'
    data_url = widget_url + report_url

    response = requests.get(data_url)

    onclick_value = "loadMetaData('SP.DYN.LE00.IN','S','Series','Life expectancy at birth, total (years)','2','1801')"
    life_expectancy_years = BeautifulSoup(response.text, 'html.parser') \
                                            .find(attrs={'onclick': onclick_value}) \
                                            .parent \
                                            .find_all('td')[-1] \
                                            .find('div').get_text()

    return life_expectancy_years
