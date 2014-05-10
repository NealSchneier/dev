import urllib2

url = "http://biz.yahoo.com/p/csv/"
sector = "1" #list of 1-9
properties = "coname"
sort = "u"
static = ".csv"

response = urllib2.urlopen(url + sector + properties + sort + static)
html = response.read()

f = open("data/industry/google.csv","w")
f.write(html)

