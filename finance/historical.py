import urllib2

url = "http://ichart.yahoo.com/table.csv?s="
security = "GOOG"
fromMonth = "&a=1"
fromDay = "&b=1"
fromYear = "&c=2000"

toMonth = "&d=1"
toDay = "&e=1"
toYear = "&f=2010"

interval = "&g=w"

static = "&ignore=.csv"

response = urllib2.urlopen(url + security + fromMonth + fromDay + fromYear + toMonth + toDay + toYear + interval + static)
html = response.read()

f = open("data/historical/google.csv","w")
f.write(html)

