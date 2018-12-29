# Scraper of the The World Bank most recent life expectancy stats
# for when the prediction based on the country is made
from bs4 import BeautifulSoup

soup = BeautifulSoup('<html><body><b>Hi</b></body></html>', 'html.parser')

print(soup.body)