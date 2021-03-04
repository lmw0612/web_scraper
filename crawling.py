from bs4 import BeautifulSoup
import re
import requests
import scrapy
import sys
import pandas as pd

# For Test purpose, only one article will be used
url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'
try:
    resp = requests.get(url)
except Exception as e:
    error_type, error_obj, error_infp
page = requests.get(url)

# TODO: Title, Category, Author Name, Day, Month, Year, Contents