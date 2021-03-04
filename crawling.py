from bs4 import  BeautifulSoup
import re
import requests
import scrapy

url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'
resp = requests.get(url)

# TODO: Title, Type, Author Name, Day, Month, Year, Contents