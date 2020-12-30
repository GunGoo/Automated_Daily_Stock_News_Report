#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
import requests

url = "https://seekingalpha.com/symbol/TSLA/income-statement"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
news = soup.find(name="div", attrs={
                 'class': "table-wrap", 'data-table-id': "revenues"})
# news = soup.find(name="div", attrs={
#                  'class': "table-wrap", 'data-table-id': "revenues"})
print(soup)
print(news)

# page_soup = soup(response, 'html.parser')
# for anchor in page_soup.find('table', id="revenues"):
#     print(anchor)
