from bs4 import BeautifulSoup, NavigableString
import requests


class Table:
    
    def __init__(self, url, forbidden):
        self.table = find_table(url)
        self.data = find_string_tags(self.table, forbidden)
        
def find_table(url):
    '''make a soup object from the requested html.
    soup is used to browse through the tags, as if it was xml.'''
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    return soup.find("table")    

 
def find_string_tags(table, forbidden):
    data = []
    for tag in table.descendants:
        if isinstance(tag, NavigableString):
            tag = tag.strip()
            if tag and not any(s in tag for s in forbidden):
                data.append(tag)
    return data

url = "https://en.wikipedia.org/wiki/List_of_circulating_currencies"
forbidden = ['(', ')', '[', 'none']

print(Table(url, forbidden).data)

