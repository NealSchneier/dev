from scriptUtils import convert, yahooFinanceAPIRequest
from mysqlUtils import getMysqlConnection

url = "http://biz.yahoo.com/p/csv/"
sector = "s_"
properties = "coname"
sort = "u"
static = ".csv"

con = getMysqlConnection()
try:
	csvReader = yahooFinanceAPIRequest(url + sector + properties + sort + static)
	
except: 
	print "Error with URL Request/ Converting CSV " +  url + sector + properties + sort + static

try:
	with con:
		cur = con.cursor()
		for row in csvReader:
			#print 'select id from sector where name="' + row['Sectors'] + '"'
			cur.execute('select id from sector where name="' + row['Sectors'] + '"')
		 	sectorId = cur.fetchone()
			#print 'insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', ' + row[3]+', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' );'
			cur.execute('insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row["1-Day Price Chg %"]+ ', ' + convert(row["Market Cap"]) +', ' + row["P/E"]+', ' + row["ROE %"]+', ' + row["Div. Yield %"]+', ' + row["Debt to Equity"]+', ' + row["Price to Book"]+', ' + row["Net Profit Margin (mrq)"]+', ' + row["Price To Free Cash Flow (mrq)"] +' );')	
		con.commit()

except db.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])

con.close()