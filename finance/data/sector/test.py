import csv

with open("all.csv", 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)

	for row in spamreader:
		print row
