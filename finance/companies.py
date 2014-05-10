import urllib2

url = "http://biz.yahoo.com/p/csv/"
industry = "112"
sort = "coname"
direction ="u"
#possible properties - https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty
static = ".csv"

response = urllib2.urlopen(url + industry + sort + direction + static)
html = response.read()

f = open("data/companies/google.csv","w")
f.write(html)

