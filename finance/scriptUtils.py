import urllib2
import MySQLdb as db
import csv

def convert(string):
	string = string.upper()
	if string.find("NA") == -1:
		if string.find("B") != -1:
			return string[:-1] + "000000000"
		if string.find("M") != -1:
			return string[:-1] + "000000"
		return string
	
	return "0"

def addFormatting(position, value):
	return "&" + position + "=" + value
	
#http://finance.yahoo.com/d/quotes.csv?s=MSFT+F+ATT&f=sn

#from symbol make request to get the name, match to the company table on db and return the company id

def getCompanyId(symbol, databaseConnection):
	url = "http://finance.yahoo.com/d/quotes.csv?s=" + symbol + addFormatting("f", "sn")
	response = urllib2.urlopen(url)

	html = response.read()
	try:
		#con = db.connect('localhost', 'root', 'metsfan', 'finance2')
		con = databaseConnection
		with con:
			cur = con.cursor()
			cnt = html.count('\n')
			html = html.split(',')
			html[1] = html[1].replace('\r\n', '')
			#print html[1]
			cur.execute('select * from company where name like ' + html[1][:len(html[1])-1] + '%"')
			companyId = cur.fetchone()
			#print companyId
			if companyId[1] is None:
				#print 'update company set symbol=' + symbol + ' where name like ' + html[1][:len(html[1])-1] + '%"'
				cur.execute('update company set symbol="' + symbol + '" where name like ' + html[1][:len(html[1])-1] + '%"')

			if companyId[2] is not None:
				return companyId[2]
			return None

	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	   
def convertCSV(csvFile):
	##with open(csvFile, 'rb') as csvfile:
	#print csvFile
	return csv.DictReader(csvFile)
#		for row in spamreader:
#		print row
