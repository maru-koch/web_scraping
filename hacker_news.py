#: install and import beautifulsoup
#: install requests
#: python 3.10.2 64 bit

#: SOUP OBJECT METHODS
#:  -   contents 
#   -   title 
#   -   find 
#   -   find_all(html_element) 
#   -   select : selects all of the specified html tag element
#   -   scraping page one and two of the hacker news website
#   -   beautifulsoup is a library suitable for scraping small website
#   -   for large scale web scraping, use scrapy (scrapy.org)

from bs4 import BeautifulSoup
import requests
import pprint

response = requests.get("https://news.ycombinator.com/news")

response2 = requests.get("https://news.ycombinator.com/news?p=2")


#: soup object
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

links = soup.select('.titlelink')
links2 = soup2.select('.titlelink')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

#: sorting the dictionary by the key vote
def sorted_list(hn_list):
    return sorted(hn_list, key = lambda x: x['vote'], reverse = True)


def hack_news(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'href': href, 'vote': points})
 
    return sorted_list(hn) 

pprint.pprint(hack_news(mega_links, mega_subtext))
