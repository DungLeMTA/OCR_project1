from pydoc import classname

import requests
from bs4 import BeautifulSoup

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
URL = 'https://hienngong.wordpress.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')
title = soup.find_all(id="infinity-blog-title")
print(title)
print(title.getText().strip())
# results.click()
# print(results.prettify())