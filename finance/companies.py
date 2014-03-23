import urllib2

url = "http://download.finance.yahoo.com/d/quotes.csv?s="
security = "%40%5EDJI,GOOG,AAPL"
properties = "&f=nsl1op"
static = "&e=.csv"

response = urllib2.urlopen(url + security + properties + static)
html = response.read()

f = open("data/companies/google.csv","w")
f.write(html)

