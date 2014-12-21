##This script needs to make the create for each company into 
##
#1 - insert company and get the id
#2 - query for the corresponding industry id
#3 - insert companyToSector for the corresponding industry + company ids

import urllib2
import MySQLdb as db
import unicodedata


def remove_accents(data):
    return ''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn'))




url = "http://biz.yahoo.com/p/csv/"
industry = [112, 132, 110, 131, 134, 121, 133, 120, 136, 123, 124, 125, 122, 135, 113, 130, 111, 210, 310, 330, 333, 346, 348, 347, 313, 350, 326, 345, 344, 314, 341, 340, 311, 312, 343, 327, 325, 324, 323, 318, 342, 317, 332, 322, 316, 320, 321, 351, 315, 331, 431, 422, 425, 426, 427, 424, 423, 417, 418, 434, 420, 421, 430, 410, 447, 432, 448, 440, 442, 443, 444, 441, 445, 446, 449, 412, 414, 411, 416, 413, 415, 419, 433, 515, 516, 513, 510, 511, 514, 512, 522, 526, 524, 523, 521, 520, 525, 527, 528, 610, 611, 633, 622, 620, 634, 636, 635, 627, 621, 632, 624, 631, 626, 623, 630, 625, 628, 637, 720, 773, 772, 730, 744, 738, 750, 758, 724, 723, 751, 760, 725, 739, 755, 763, 731, 732, 733, 756, 766, 735, 753, 722, 757, 714, 716, 734, 737, 736, 752, 742, 710, 770, 769, 721, 754, 726, 743, 762, 729, 727, 728, 776, 771, 761, 768, 711, 712, 765, 775, 713, 745, 715, 740, 764, 767, 741, 774, 759, 821, 826, 841, 812, 815, 813, 846, 810, 836, 825, 827, 824, 851, 850, 852, 843, 820, 814, 811, 835, 842, 837, 823, 833, 832, 834, 831, 822, 833, 845, 840, 913, 911, 910, 912, 914]	 #full list here - http://pastie.org/6419646
#industry = [123]
sort = "coname"
direction ="u"
#possible properties - https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty
static = ".csv"

for i in industry:
	response = urllib2.urlopen(url + str(i) + sort + direction + static)
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
			for x in range(2,cnt-1):
				html = html.partition('\n')

		 		single = html[2].partition('\n')
		 		#print "single" + single[0]
		 		row = single[0].rsplit(' \",')
		 		#print "row " + row
		 		if len(row) == 1:
		 				
		 			rest = row[0].rsplit(',')
			 		#print row
			 		#print "rest" + rest[0]
			 		html = html[2]
			 		rest[0] = remove_accents(rest[0].decode('utf-8'))
			 		print len(rest[0][0])
			 		#tempRest = rest[0]
			 		#rest[0] = rest[0].rstrip("\n")
			 		#print rest[0].replace('o', '')
			 		
			 		#	rest[0] = rest[0].replace(rest[0], "\n", 1)
			 		if rest[0].count('"') == 1:
			 			try:
			 				print 'insert into company (name) values (' + rest[0] + '")'
			 				cur.execute('insert into company (name) values (' + rest[0] + '")')
 							
							cur.execute('select id from company where name=' + rest[0] + '"')
							companyId = cur.fetchone()
							print companyId[0]
							cur.execute('insert into companyToSector (industry_id, company_id) values (' + str(i) + ', ' + str(companyId[0]) + ')')
						except db.IntegrityError:
							print "duplicate 1"
			 		elif len(rest) == 10:
			 			try:
			 				print 'insert into company (name) values (' + rest[0] + ')'
			 				cur.execute('insert into company (name) values (' + rest[0] + ')')
 							
							cur.execute('select id from company where name=' + rest[0] + '')
							companyId = cur.fetchone()
							print companyId[0]
							cur.execute('insert into companyToSector (industry_id, company_id) values (' + str(i) + ', ' + str(companyId[0]) + ')')
						except db.IntegrityError:
							print "duplicate 1"
			 		elif len(rest) == 11:
			 			try: 
			 				print 'insert into company (name) values (' + rest[0] + rest[1]+ ')'
			 				cur.execute('insert into company (name) values (' + rest[0] + rest[1]+ ')')
							cur.execute('select id from company where name=' + rest[0] + rest[1]+ '')
							companyId = cur.fetchone()
							print companyId[0]
							cur.execute('insert into companyToSector (industry_id, company_id) values (' + str(i) + ', ' + str(companyId[0]) + ')')
						except db.IntegrityError:
							print "duplicate 2"
			 		elif len(rest) == 12:
			 			try:
			 				print 'insert into company (name) values (' + rest[0] + rest[1] + rest[2] + ')'
			 				cur.execute('insert into company (name) values (' + rest[0] + rest[1] + rest[2] + ')')
							cur.execute('select id from company where name=' + rest[0] + rest[1] + rest[2] + '')
							companyId = cur.fetchone()
							print companyId[0]
							cur.execute('insert into companyToSector (industry_id, company_id) values (' + str(i) + ', ' + str(companyId[0]) + ')')
						except db.IntegrityError:
							print "duplicate 3"

	except db.Error, e:
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    #sys.exit(1)
	    
	finally:    
	        
	    if con:    
	        con.close()
	#except:
	#	print "Error on URL Request"

#f = open("data/industry/google.csv","w")
#f.write(html)

