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
import pprint

response = requests.get("https://news.ycombinator.com/news")


#: soup object
soup = BeautifulSoup(response.text, 'html.parser') 
links = soup.select('.titlelink')
subtext = soup.select('.subtext')
def hack_news(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            hn.append({'title': title, 'href': href, 'vote': points})
            
    return hn 

pprint.pprint(hack_news(links, subtext))
