"""
    This number counts the highest number of occuring 
    words on a web page
"""

import requests
from bs4 import BeautifulSoup

url = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.getText()