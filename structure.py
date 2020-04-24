from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.error

#  Here we add the tags we wat to scrap from the site
# tag = input('Tag : ')
# class_ = input('Class : ')
try:
    html = urlopen(input('Enter a Url >>> '))
except urllib.error.HTTPError as e:
    print(e)
else:
    soup = BeautifulSoup(html.read(), 'html.parser')
    #print(soup.prettify())
    print('Its end here!')
    all = soup.find('div', {'class': 'carousel slide'})
    for i in all:
        print(all.find_all('isolategit'))
    #for i in soup.find_all('div', {'class': 'container-scrollbar.ng-isolate-scope.mCustomScrollbar._mCS_2'}):
        #print(soup)
    #   # print(soup.prettify())
