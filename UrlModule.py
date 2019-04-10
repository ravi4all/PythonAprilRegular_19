import urllib.request as url
import bs4

path = "https://www.cricbuzz.com"

httpResponse = url.urlopen(path)
page = bs4.BeautifulSoup(httpResponse, 'lxml')

imgs = page.find_all("img")

#url.urlretrieve('https://www.cricbuzz.com/i/news/fth/420x235/images/homepage/qck_1554859056.jpeg','image_1.jpg')

for i in range(len(imgs)):
    if i == 1:
        continue
    imgUrl = path + imgs[i]['src']
    print(imgUrl)
    url.urlretrieve(imgUrl, 'img_{}'.format(i)+".png")
print("Download Complete....")
