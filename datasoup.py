from bs4 import BeautifulSoup
import requests

url = 'https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1'

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
buttons = soup.find_all('button')

p = []
for item in buttons:
    if item.text.isdigit() and len(item.text) <= 3:
        print(item)
        p.append(item.text)
if p:
    lastPage = int(p.pop())
else:
    lastPage = 1

print(lastPage)

import re
url = 'https://www.immoscout24.ch/en/house/buy/city-bern?pn=1&r=7&se=16&map=1'

ids = []
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
links = soup.find_all('a', href=True)
hrefs = [item['href'] for item in links]
hrefs_filtered = [href for href in hrefs if href.startswith('/en/d')]
ids += [re.findall('\d+', item)[0] for item in hrefs_filtered]

print(ids)