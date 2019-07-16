import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/";
r_html = requests.get(url).text

soup = BeautifulSoup(r_html,"html.parser")
title = soup.find('div','collection')
print(title)