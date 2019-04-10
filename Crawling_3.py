# bs4 - Beautiful Soup - returns source code of that page from where you want
# to fetch the data
import bs4
# urllib.request - we hit any website and in return it gives http response
# so we make a http request using this module
# if a webpage return http response then we can crawl the data
import urllib.request as url

path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="
userInput = input("Enter movie name : ")
httpResponse = url.urlopen(path+userInput)
page = bs4.BeautifulSoup(httpResponse, 'lxml')

td = page.find('td', class_='result_text')
href = td.find('a')['href']
#print(href)

newUrl = "https://www.imdb.com"+href
httpResponse = url.urlopen(newUrl)
page_2 = bs4.BeautifulSoup(httpResponse, 'lxml')
div = page_2.find('div',class_='title_wrapper')
#print(div.text)
div = div.text.replace("\n","")
div = div.split()
title = " ".join(div)
print(title)

summary = page_2.find('div', id='titleStoryLine')
para = summary.find('p')
print(para.text)

links = page_2.find('div', id='quicklinksMainSection')
reviewhref = links.find_all('a')[2]['href']

newUrl = "https://www.imdb.com"+reviewhref
httpResponse = url.urlopen(newUrl)
page_3 = bs4.BeautifulSoup(httpResponse, 'lxml')
titles = page_3.find_all('a', class_='title', limit=3)
for i in range(len(titles)):
    print(titles[i].text)
