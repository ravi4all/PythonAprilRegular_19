import bs4
import urllib.request as url

request  = url.urlopen('https://www.cricbuzz.com/')
#print(request)
data = bs4.BeautifulSoup(request, 'lxml')

a = data.find_all('a', class_='cb-nws-hdln-ancr')
#print(a)
'''
for i in range(len(a)):
    print(a[i].text)
'''
'''
for news in a:
    print(news.text)
'''

for i,news in enumerate(a, start=1):
    print(i,news.text)
