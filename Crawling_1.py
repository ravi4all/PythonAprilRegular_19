import bs4
import urllib.request as url

request  = url.urlopen('https://timesofindia.indiatimes.com/')
#print(request)
data = bs4.BeautifulSoup(request, 'lxml')
div = data.find('div', id='featuredstory')
print(div.text.strip())

ul = data.find('ul', class_='list8')
print(ul.text.replace("\n\n","\n"))
