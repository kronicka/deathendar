# Scraper of the The World Bank most recent life expectancy stats
# for when the prediction based on the country is made
from bs4 import BeautifulSoup
import requests

country = 'RUS'
widget_url = 'https://databank.worldbank.org/data/views/reports/reportwidget.aspx'
report_url = f'?Report_Name=CountryProfile&Id=b450fd57&tbar=y&dd=y&inf=n&zm=n&country={country}'
data_url = widget_url + report_url

response = requests.get(data_url)

onclick_value = "loadMetaData('SP.DYN.LE00.IN','S','Series','Life expectancy at birth, total (years)','2','1801')"
soup = BeautifulSoup(response.text, 'html.parser') \
                    .find(attrs={'onclick': onclick_value}) \
                    .parent \
                    .find_all('td')[-1] \
                    .find('div').get_text()

print(soup)
