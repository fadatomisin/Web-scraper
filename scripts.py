from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()