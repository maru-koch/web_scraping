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
links = soup.select('.storylink')
votes = soup.select('.score')
def hack_news(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = votes[idx].getText()
        hn.append({'title': title, 'href': href})
    return hn

print(hack_news(links, votes))
