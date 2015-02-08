from scriptUtils import convert, yahooFinanceAPIRequest
from mysqlUtils import getMysqlConnection
import time

url = "http://biz.yahoo.com/p/csv/"
industry = [112, 132, 110, 131, 134, 121, 133, 120, 136, 123, 124, 125, 122, 135, 113, 130, 111, 210, 310, 330, 333, 346, 348, 347, 313, 350, 326, 345, 344, 314, 341, 340, 311, 312, 343, 327, 325, 324, 323, 318, 342, 317, 332, 322, 316, 320, 321, 351, 315, 331, 431, 422, 425, 426, 427, 424, 423, 417, 418, 434, 420, 421, 430, 410, 447, 432, 448, 440, 442, 443, 444, 441, 445, 446, 449, 412, 414, 411, 416, 413, 415, 419, 433, 515, 516, 513, 510, 511, 514, 512, 522, 526, 524, 523, 521, 520, 525, 527, 528, 610, 611, 633, 622, 620, 634, 636, 635, 627, 621, 632, 624, 631, 626, 623, 630, 625, 628, 637, 720, 773, 772, 730, 744, 738, 750, 758, 724, 723, 751, 760, 725, 739, 755, 763, 731, 732, 733, 756, 766, 735, 753, 722, 757, 714, 716, 734, 737, 736, 752, 742, 710, 770, 769, 721, 754, 726, 743, 762, 729, 727, 728, 776, 771, 761, 768, 711, 712, 765, 775, 713, 745, 715, 740, 764, 767, 741, 774, 759, 821, 826, 841, 812, 815, 813, 846, 810, 836, 825, 827, 824, 851, 850, 852, 843, 820, 814, 811, 835, 842, 837, 823, 833, 832, 834, 831, 822, 833, 845, 840, 913, 911, 910, 912, 914]	 #full list here - http://pastie.org/6419646
#industry = [112]
sort = "coname"
direction ="u"
#possible properties - https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty
static = ".csv"
con = getMysqlConnection()

for i in industry:
	csvReader = yahooFinanceAPIRequest(url + str(i) + sort + direction + static)
	try:
		with con:
		 	cur = con.cursor()
		 	
		 	for row in csvReader:
	 			cur.execute('select id from company where name="' + row["Description"] + '"')
				companyId = cur.fetchone()
				if companyId is None:
					cur.execute('insert into company (name) values ("' + row["Description"] + '")')
					cur.execute('select id from company where name="' + row["Description"] + '"')
					companyId = cur.fetchone()

					#the insert the convert table
					cur.execute('select id from companyToIndustry where company_id=' + str(companyId[0]) + '')
					companyToIndustry = cur.fetchone()
					if companyToIndustry is None:
						cur.execute('insert into companyToIndustry (company_id, industry_id) values (' + str(companyId[0]) 
							+ ", " + str(companyToIndustry[0]) + ')')
				#print companyId[0]
	 			#print str(rest[0]) + ', ' + convert(rest[1])+ ', "' + convert(rest[2]) +'", "' + convert(rest[3])+'", ' + convert(rest[4])+', ' + convert(rest[5])+', ' + convert(rest[6])+', ' + convert(rest[7])+', ' + convert(rest[8])+', ' + convert(rest[9]) 
	 			cur.execute('insert into companies (company_id, day_price_change, market_cap , price_to_earnings_ratio, roe_percent, div_yield_percent, debt_to_equity, price_to_book, net_profit_margin, price_to_free_cash_flow) values ('+ str(companyId[0]) + ', ' + convert(row["1-Day Price Chg %"])+ ', "' + convert(row["Market Cap"]) +'", "' + convert(row["P/E"])+'", ' + convert(row["ROE %"])+', ' + convert(row["Div. Yield %"])+', ' + convert(row["Debt to Equity"])+', ' + convert(row["Price to Book"])+', ' + convert(row["Net Profit Margin (mrq)"])+', ' + convert(row["Price To Free Cash Flow (mrq)"]) +' )')
				con.commit()
	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	
con.close()




