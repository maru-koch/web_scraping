#: install and import beautifulsoup
#: install requests
#: python 3.10.2 64 bit

#: SOUP OBJECT METHODS
#:  -   contents 
#   -   title 
#   -   find 
#   -   find_all(html_element) 
#   -   select : selects all of the specified html tag element

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

#: soup object
soup = BeautifulSoup(response.text, 'html.parser')
scores = soup.find_all('a')
links = soup.select('.storylink')
votes = soup.select('score')
# for index, score in enumerate(scores, start = 1):
#     print("--------------------------")
#     print(f"{index} -- {score}")

