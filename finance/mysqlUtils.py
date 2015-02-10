import MySQLdb as db

def getMysqlConnection():
	return db.connect('localhost', 'root', 'metsfan', 'finance2')

