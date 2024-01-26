# IN PROGRESS

import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
data = soup.find_all("div", class_="facts-wrapper")

data_set = {}
for i in data:
    data_set.update({"category": i.h5.text})


print(data_set)