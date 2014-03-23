import urllib2

url = "http://biz.yahoo.com/p/csv/"
sector = "s_"
properties = "coname"
sort = "u"
static = ".csv"

response = urllib2.urlopen(url + sector + properties + sort + static)
html = response.read()

f = open("data/sector/all.csv","w")
f.write(html)

