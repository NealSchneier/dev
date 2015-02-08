from scriptUtils import convert, yahooFinanceAPIRequest
from mysqlUtils import getMysqlConnection
import time

url = "http://biz.yahoo.com/p/csv/"
sector = range(1, 10) #list of 1-9
properties = "coname"
sort = "u"
static = ".csv"

for i in sector:
	time.sleep(5)
	try:
		csvReader = yahooFinanceAPIRequest(url + str(i) + properties + sort + static)
	except: 
		print "Error with URL Request/ Converting CSV " +  url + str(i) + properties + sort + static
	con = None
	try:
		con = getMysqlConnection()
		with con:
			cur = con.cursor()
			for row in csvReader:
				#print row
				print 'select id from industry where name="' + row["Industry"] + '"'
				cur.execute('select id from industry where name="' + row["Industry"] + '"')	
				industryId = cur.fetchone()
				#If the industry is not present then create it
				if industryId is None:
					print 'insert into industry (name, sector_id) values ("' + row["Industry"] + '", ' + str(i) + ')'
					cur.execute('insert into industry (name, sector_id) values ("' + row["Industry"] + '", ' + str(i) + ')')

					print 'select id from industry where name="' + row["Industry"] + '"'
					cur.execute('select id from industry where name="' + row["Industry"] + '"')
					industryId = cur.fetchone()

				print 'insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row["1-Day Price Chg %"]+ ', ' + convert(row["Market Cap"]) +', "' + row["P/E"]+'", ' + row["ROE %"]+', ' + convert(row["Div. Yield %"])+', ' + convert(row["Debt to Equity"])+', ' + row["Price to Book"]+', ' + row["Net Profit Margin (mrq)"]+', ' + row["Price To Free Cash Flow (mrq)"] +' )'
				cur.execute('insert into industries (sector_number, industry, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(i) + ', '+ str(industryId[0]) + ', ' + row["1-Day Price Chg %"]+ ', ' + convert(row["Market Cap"]) +', "' + row["P/E"]+'", ' + row["ROE %"]+', ' + convert(row["Div. Yield %"])+', ' + convert(row["Debt to Equity"])+', ' + row["Price to Book"]+', ' + row["Net Profit Margin (mrq)"]+', ' + row["Price To Free Cash Flow (mrq)"] +' )')

	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	   
	finally:    
	        
	    if con:    
	        con.close()