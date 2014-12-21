import urllib2
import MySQLdb as db
from scriptUtils import convert, addFormatting, getCompanyId
import datetime
import time
from dateutil.parser import parse

url = "http://ichart.yahoo.com/table.csv?s="
# security = "GOOG"
# fromMonth = "&a=1"
# fromDay = "&b=1"
# fromYear = "&c=2000"

# toMonth = "&d=1"
# toDay = "&e=1"
# toYear = "&f=2010"

# interval = "&g=w"

static = "&ignore=.csv"

#response = urllib2.urlopen(url + security + fromMonth + fromDay + fromYear + toMonth + toDay + toYear + interval + static)
#html = response.read()



def getHistoricalQuotes(security, fromMonth, fromDay, fromYear, toMonth, toDay, toYear, interval):
	response = urllib2.urlopen(url + security + addFormatting("a", fromMonth) + addFormatting("b", fromDay) 
		+ addFormatting("c", fromYear) + addFormatting("d", toMonth) + addFormatting("e", toDay) 
		+ addFormatting("f", toYear) + addFormatting("g", interval) + static)

	html = response.read()
	try:
		con = db.connect('localhost', 'root', 'metsfan', 'finance2')
		with con:
			cur = con.cursor()
			cnt = html.count('\n')
			companyId = getCompanyId(security)
			
			for x in range(cnt-1):
				html = html.partition('\n')
				single = html[2].partition('\n')
				row = single[0].rsplit(',')
				#print row
				html = html[2]
				#time.strftime('%Y-%m-%d')
				dateMysql = datetime.datetime(int(row[0][:4]), int(row[0][5:7]), int(row[0][8:10]))
				#print row[0] + row[0][:4] + row[0][5:7] + row[0][8:10]
				#print str(x) + " " + row[0]
				dateMysql = dateMysql.strftime('%Y-%m-%d')
				
				try:
					if companyId is not None:
						cur.execute('insert into quotes (company_id, quote_date, open, high, low, close, volume, adj) ' 
							+ 'values ( ' + str(companyId) + ', date("' + dateMysql +'"), ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', '
							+ row[4] + ', ' + row[5] + ', ' + row[6] +')')
					else:
						cur.execute('insert into quotes (quote_date, open, high, low, close, volume, adj) ' 
							+ 'values (date("' + dateMysql +'"), ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', '
							+ row[4] + ', ' + row[5] + ', ' + row[6] +')')
				except db.Error, e:
					print str(x) +  'insert into quotes (company_id, quote_date, open, high, low, close, volume, adj) ' 
					+ 'values ( ' + str(companyId) + 'date("' + dateMysql +'"), ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', '
					+ row[4] + ', ' + row[5] + ', ' + row[6] +')'
			
	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    #sys.exit(1)
	    #print  str(i) + ', '+ row[0] + ', ' + row[1]+ ', "' + row[2] +'", "' + row[3]+'", ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] 
	    
	finally:    
	        
	    if con:    
	        con.close()

print getHistoricalQuotes('IBM', '1', '1', '2009', '1', '1', '2010', 'w')

