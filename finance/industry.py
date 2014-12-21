import urllib2
import MySQLdb as db
from scriptUtils import convert

url = "http://biz.yahoo.com/p/csv/"
sector = range(1, 10) #list of 1-9
properties = "coname"
sort = "u"
static = ".csv"

for i in sector:
	response = urllib2.urlopen(url + str(i) + properties + sort + static)
	#try:
	#	response = urllib2.urlopen(url + str(i) + properties + sort + static)
		
		#connect with database
	try:
		html = response.read()
#		con = db.connect('localhost', '', 'Metsfan8669', 'finance')
		con = db.connect('localhost', 'root', 'metsfan', 'finance2')
		with con:
			cur = con.cursor()
			cnt = html.count('\n')
			for x in range(cnt-1):
				html = html.partition('\n')
				single = html[2].partition('\n')
				row = single[0].rsplit(',')
				#print row
				html = html[2]
				
				if len(row) == 10:
					cur.execute('select id from industry where name=' + row[0] + '')
					
					industryId = cur.fetchone()
					if industryId is None:
						cur.execute('insert into industry (name, sector_id) values (' + row[0] + ', ' + str(i) + ')')
						cur.execute('select id from industry where name=' + row[0] + '')
						industryId = cur.fetchone()
					#print 'insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', "' + row[3]+'", ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' )'
					cur.execute('insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', "' + row[3]+'", ' + row[4]+', ' + convert(row[5])+', ' + convert(row[6])+', ' + row[7]+', ' + row[8]+', ' + row[9] +' )')
				else: 
					cur.execute('select id from industry where name=' + row[0] + row[1]+ '')
					industryId = cur.fetchone()

					if industryId is None:
						cur.execute('insert into industry (name, sector_id) values (' + row[0] + row[1] + ', ' + str(i) + ')')
						cur.execute('select id from industry where name=' + row[0] + row[1]+ '')
						industryId = cur.fetchone()
					#print 'insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row[2] +', ' + convert(row[3]) +', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +', ' + row[10] +')'
					cur.execute('insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row[2] +', ' + convert(row[3]) +', ' + row[4]+', ' + row[5]+', ' + convert(row[6])+', ' + convert(row[7]) +', ' + row[8]+', ' + row[9] +', ' + row[10] +')')
	
	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    #sys.exit(1)
	    #print  str(i) + ', '+ row[0] + ', ' + row[1]+ ', "' + row[2] +'", "' + row[3]+'", ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] 
	    
	finally:    
	        
	    if con:    
	        con.close()
	#except:
	#	print "Error on URL Request"

#f = open("data/industry/google.csv","w")
#f.write(html)

