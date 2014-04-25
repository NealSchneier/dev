from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen('http://www.shopstyle.com/action/rawProducts?size=Large&count=4000&min=1')
html = response.read()
soup = BeautifulSoup(html)

#soup = soup.find(id="browsePage1ContentDiv")
count = 0
for link in soup.find_all("img", {"class": 'cellImg'}):
	print link.get("src")
	count += 1
print count