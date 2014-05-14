import urllib2
import MySQLdb as db


url = "http://biz.yahoo.com/p/csv/"
sector = "s_"
properties = "coname"
sort = "u"
static = ".csv"
try: 
	response = urllib2.urlopen(url + sector + properties + sort + static)
	html = response.read()
	
except: 
	print "Error with URL Request"


#connect with database
try:
	#con = db.connect('finance.c0yndj7oh9sl.us-west-2.rds.amazonaws.com', 'neal', 'Metsfan8669', 'finance')
	con = db.connect('localhost', 'root', 'metsfan', 'finance')
	with con:
		cur = con.cursor()
		cnt = html.count('\n')
		for i in range(cnt-1):
			html = html.partition('\n')
			single = html[2].partition('\n')
			row = single[0].rsplit(',')
			html = html[2]
			cur.execute('insert into sector (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + row[0] + ', ' + row[1]+ ', "' + row[2]+'", ' + row[3]+', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' );')
	
except db.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    #sys.exit(1)
    
finally:    
        
    if con:    
        con.close()

#f = open("data/sector/all.csv","w")
#f.write(html)

