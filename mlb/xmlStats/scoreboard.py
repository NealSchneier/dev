import urllib2, json, datetime
import time, sys, subprocess, shlex
import insert

REQUEST = "Bearer 86e981fb-1415-4001-9aad-098d77bce811"
URL = "https://erikberg.com/"


def get_scoreboard(date):
	r = urllib2.Request(URL + "events.json?date=" + date + "&sport=mlb")
	r.add_header('Authorization', REQUEST)
	r.add_header("Accept-encoding", "-compressed")
	try:
		f = urllib2.urlopen(r)
		output = json.loads(f.read())
		with open(date + ".scoreboard", 'wr') as outfile:
	  		json.dump(output, outfile)
	except:
		print "error on scoreboard for " + date

def get_boxscore(date, awayTeam, homeTeam):
	r = urllib2.Request(URL + "mlb/boxscore/" + date + "-" + awayTeam + "-at-" + homeTeam + ".json")

	r.add_header('Accept-encoding', '--compressed')
	f = None
	filename = ""
	try:
		f = urllib2.urlopen(r)
		output = json.loads(f.read())
		filename = "boxscore-" + date + "-" + awayTeam + "-at-" + homeTeam
		with open(filename, 'w') as outfile:
			json.dump(output, outfile)
	except urllib2.HTTPError:
		print date + " " + awayTeam + " at " + homeTeam + " postponed"
		filename = "postponed"
	return filename

def run_scoreboard():

	start = time.asctime()
	#monday = (datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y%m%d")
 	tuesday = (datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y%m%d")
 	wednesday = (datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y%m%d")
 	thursday = (datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y%m%d")
 	friday = (datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y%m%d")
 	saturday = (datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y%m%d")
 	sunday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y%m%d")

	#get_scoreboard(monday)
	#time.sleep(10)
	get_scoreboard(tuesday)
	time.sleep(10)
	get_scoreboard(wednesday)
	time.sleep(10)
	get_scoreboard(thursday)
	time.sleep(10)
	get_scoreboard(friday)
	time.sleep(10)
	get_scoreboard(saturday)
	time.sleep(10)
	get_scoreboard(sunday)
	print "start insert"
	# insert.scoreboard(monday)
	# print time.asctime()
	insert.scoreboard(tuesday)
	print time.asctime()
	insert.scoreboard(wednesday)
	print time.asctime()
	insert.scoreboard(thursday)
	print time.asctime()
	insert.scoreboard(friday)
	print time.asctime()
	insert.scoreboard(saturday)
	print time.asctime()
	insert.scoreboard(sunday)
	print time.asctime()

def run_boxscore():
	start = time.asctime()
	#one = (datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y%m%d")
	two = (datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y%m%d")
	three = (datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y%m%d")
	four = (datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y%m%d")
	five = (datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y%m%d")
	six = (datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y%m%d")
	seven = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y%m%d")

	# date = one
	# games = insert.get_games(one)
	# for game in games:
	# 	filename = get_boxscore(date, game[0], game[1])
	# 	if filename != "postponed":
	# 		insert.boxscore(filename)
	# 		time.sleep(10)
	date = two
	games = insert.get_games(two)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)
	date = three
	games = insert.get_games(three)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)
	date = four
	games = insert.get_games(four)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)
	date = five
	games = insert.get_games(five)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)
	date = six
	games = insert.get_games(six)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)
	date = seven
	games = insert.get_games(seven)
	for game in games:
		filename = get_boxscore(date, game[0], game[1])
		if filename != "postponed":
			insert.boxscore(filename)
			time.sleep(10)


def clean():
	cmd = "rm -f boxscore* 20*"
	arg = shlex.split(cmd)
	subprocess.Popen(cmd, shell=True)


run_scoreboard()

run_boxscore()

clean()


