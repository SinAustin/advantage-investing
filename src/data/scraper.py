import bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def go():
    a = str(datetime.now().month)
    b = str(datetime.now().day -1)
    c = str(datetime.now().year -1)
    d = str(datetime.now().year)
    yesterday = a + '/' + b + '/' + d
    last_year = a + '/' + b + '/' + c
    return yesterday, last_year
