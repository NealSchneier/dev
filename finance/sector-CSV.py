import urllib2
import MySQLdb as db
from scriptUtils import convert, convertCSV
from mysqlUtils import getMysqlConnection

url = "http://biz.yahoo.com/p/csv/"
sector = "s_"
properties = "coname"
sort = "u"
static = ".csv"

try:
	response = urllib2.urlopen(url + sector + properties + sort + static)

	csvReader = convertCSV(response.read())
	
except: 
	print "Error with URL Request/ Converting CSV " +  url + sector + properties + sort + static


#connect with database
try:
	#get a Connection
	# con = mysqlUtils.getMysqlConnection()
	# with con:
	# 	cur = con.cursor()
	# 	for i in csvReader:

	# 		#get the id for the sector
	# 		cur.execute('select id from sector where name=' + row[0] + '')
	# 		sectorId = cur.fetchone()
			#print 'insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', ' + row[3]+', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' );'
			#cur.execute('insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', ' + row[3]+', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' );')

	## The dict columns
	##"Sectors","1-Day Price Chg %","Market Cap","P/E","ROE %","Div. Yield %","Debt to Equity","Price to Book","Net Profit Margin (mrq)","Price To Free Cash Flow (mrq)"		
	
	con = getMysqlConnection()
	with con:
		cur = con.cursor()
		for row in csvReader:
			print 'select id from sector where name="' + row['Sectors'] + '"'
			cur.execute('select id from sector where name="' + row['Sectors'] + '"')
		 	sectorId = cur.fetchone()
			#print 'insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row[1]+ ', ' + convert(row[2]) +', ' + row[3]+', ' + row[4]+', ' + row[5]+', ' + row[6]+', ' + row[7]+', ' + row[8]+', ' + row[9] +' );'
			cur.execute('insert into sectors (sector, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values (' + str(sectorId[0]) + ', ' + row["1-Day Price Chg %"]+ ', ' + convert(row["Market Cap"]) +', ' + row["P/E"]+', ' + row["ROE %"]+', ' + row["Div. Yield %"]+', ' + row["Debt to Equity"]+', ' + row["Price to Book"]+', ' + row["Net Profit Margin (mrq)"]+', ' + row["Price To Free Cash Flow (mrq)"] +' );')	
	con.close()

except db.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    #sys.exit(1)


#f = open("data/sector/all.csv","w")
#f.write(html)


