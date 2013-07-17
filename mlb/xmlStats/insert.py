import json, MySQLdb as mdb
import datetime
import random

global con

def start():
	global con
	con = None
	try:

    		con = mdb.connect('localhost', 'root', 'metsfan', 'mlb')
        	cur = con.cursor()
		return cur
#		cur.execute("select * from team")
	except _mysql.Error, e:

		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


def scoreboard(js):

	cur = start()
	temp = js
	f = open(js + '.scoreboard', 'r')
	js = json.loads(f.readline())
	#js = f.readline()
	f.close()
	events = js["event"]

	for event in events:
		#select away team id, home team id,
		cur.execute("select id from fantasy_game where event_id = %s", event["event_id"])
		if cur.fetchone() is None:

			away = event["away_team"]["abbreviation"]
			home = event["home_team"]["abbreviation"]
			site = event["site"]["name"]
			cur.execute("select id from fantasy_team where abbreviation = '"+ away + "'")
			away = cur.fetchone()
			cur.execute("select id from fantasy_team where abbreviation = '" + home + "'")
			home = cur.fetchone()
			cur.execute("select id from fantasy_site where name = '" + site + "'")
			site = cur.fetchone()
			date = event["event_id"][:8]


			cur.execute("insert into fantasy_game (event_id, season_type, site_id, away_id, home_id, event_status, sport, date) values "
				+"(%s, %s, %s, %s, %s, %s, %s, %s)", (event["event_id"], event["season_type"], int(site[0]), int(away[0]),
				int(home[0]), event["event_status"], event["sport"], date))
	league_games(cur, temp)
	con.commit()
	con.close()

def get_games(date):
	cur = start()
	cur.execute("select t1.team_id as away, t2.team_id as home from fantasy_game join " +
		"fantasy_team t1 on (fantasy_game.away_id = t1.id) join fantasy_team t2 on " +
		"(fantasy_game.home_id = t2.id)  where date = %s order by fantasy_game.id", date)
	temp = cur.fetchall()
	con.commit()
	con.close()
	return temp

def boxscore(filename):
	cur = start()

	f = open(filename, "r")
	output = json.loads(f.readline())
	f.close()
	home = output["home_team"]["abbreviation"]
	cur.execute("select id from fantasy_team where abbreviation = %s", home)
	home = cur.fetchone()[0]

	away = output["away_team"]["abbreviation"]
	cur.execute("select id from fantasy_team where abbreviation = %s", away)
	away = cur.fetchone()[0]

	pitchersId = []
	awayPitchers = output["away_pitchers"]
	#insert away pitchers
	for pitcher in awayPitchers:
		cur.execute("insert into fantasy_pitcher (last_name, win, runs_allowed, hit_by_pitch, walks, intentional_walks, whip, first_name, "+
			"errors, display_name, pitches_strikes, innings_pitched, save, era, wild_pitches, home_runs_allowed, pitch_order, hits_allowed, "+
			"loss, earned_runs, team_abbreviation_id, pitch_count, strike_outs) values " +
			"(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (pitcher["last_name"],
			str(pitcher["win"]), pitcher["runs_allowed"], pitcher["hit_by_pitch"], pitcher["walks"], pitcher["intentional_walks"],
			pitcher["whip"], pitcher["first_name"], pitcher["errors"], pitcher["display_name"], pitcher["pitches_strikes"],
			pitcher["innings_pitched"], str(pitcher["save"]), pitcher["era"], pitcher["wild_pitches"], pitcher["home_runs_allowed"],
			pitcher["pitch_order"], pitcher["hits_allowed"], str(pitcher["loss"]), pitcher["earned_runs"], away,
			pitcher["pitch_count"], pitcher["strike_outs"]))
		pitchersId.append(cur.lastrowid)
	homePitchers = output["home_pitchers"]
	for pitcher in homePitchers:
		cur.execute("insert into fantasy_pitcher (last_name, win, runs_allowed, hit_by_pitch, walks, intentional_walks, whip, first_name, errors, "
			+"display_name, pitches_strikes, innings_pitched, save, era, wild_pitches, home_runs_allowed, pitch_order, hits_allowed, "+
			"loss, earned_runs, team_abbreviation_id, pitch_count, strike_outs) values " +
			"(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
			(pitcher["last_name"], str(pitcher["win"]), pitcher["runs_allowed"], pitcher["hit_by_pitch"], pitcher["walks"],
			pitcher["intentional_walks"], pitcher["whip"], pitcher["first_name"], pitcher["errors"], pitcher["display_name"],
			pitcher["pitches_strikes"], pitcher["innings_pitched"], str(pitcher["save"]), pitcher["era"], pitcher["wild_pitches"],
			pitcher["home_runs_allowed"], pitcher["pitch_order"], pitcher["hits_allowed"], str(pitcher["loss"]),
			pitcher["earned_runs"], home, pitcher["pitch_count"], pitcher["strike_outs"]))
		pitchersId.append(cur.lastrowid)


	batter = output["away_batter_totals"]
	cur.execute("insert into fantasy_batter_totals(sac_hits, slg_string, rbi_with_two_outs, batting_highlights, sac_flies, total_bases, caught_stealing, "
		+"hit_by_pitch, home_runs, avg_string, avg, extra_base_hits, at_bats, left_on_base, plate_appearances_per_home_run, walks, ops_string, "
		+"stolen_base_average, triples, ops, singles, stolen_bases, runs, plate_appearances_per_rbi, doubles, plate_appearances, "+
		"at_bats_per_home_run, obp_string, hits, at_bats_per_rbi, strikeout_rate, sacrifices, walk_rate, rbi, strike_outs, slg, obp) values " +
		"(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " +
		"%s, %s, %s, %s, %s, %s, %s, %s)", (batter["sac_hits"], batter["slg_string"], batter["rbi_with_two_outs"], batter["batting_highlights"],
		batter["sac_flies"], batter["total_bases"], batter["caught_stealing"], batter["hit_by_pitch"], batter["home_runs"], batter["avg_string"],
		batter["avg"], batter["extra_base_hits"], batter["at_bats"], batter["left_on_base"], batter["plate_appearances_per_home_run"],
		batter["walks"], batter["ops_string"], batter["stolen_base_average"], batter["triples"], batter["ops"], batter["singles"],
		batter["stolen_bases"], batter["runs"], batter["plate_appearances_per_rbi"], batter["doubles"], batter["plate_appearances"],
		batter["at_bats_per_home_run"], batter["obp_string"], batter["hits"], batter["at_bats_per_rbi"], batter["strikeout_rate"],
		batter["sacrifices"], batter["walk_rate"], batter["rbi"], batter["strike_outs"], batter["slg"], batter["obp"]))
	away_batters = cur.lastrowid
	batter = output["home_batter_totals"]
	cur.execute("insert into fantasy_batter_totals(sac_hits, slg_string, rbi_with_two_outs, batting_highlights, sac_flies, total_bases, "+
		"caught_stealing, hit_by_pitch, home_runs, avg_string, avg, extra_base_hits, at_bats, left_on_base, plate_appearances_per_home_run, "
		+ "walks, ops_string, stolen_base_average, triples, ops, singles, stolen_bases, runs, plate_appearances_per_rbi, doubles, "+
		"plate_appearances, at_bats_per_home_run, obp_string, hits, at_bats_per_rbi, strikeout_rate, sacrifices, walk_rate, rbi, strike_outs, "
		+"slg, obp) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
		+"%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", (batter["sac_hits"], batter["slg_string"], batter["rbi_with_two_outs"],
		batter["batting_highlights"], batter["sac_flies"], batter["total_bases"], batter["caught_stealing"], batter["hit_by_pitch"],
		batter["home_runs"], batter["avg_string"], batter["avg"], batter["extra_base_hits"], batter["at_bats"], batter["left_on_base"],
		batter["plate_appearances_per_home_run"], batter["walks"], batter["ops_string"], batter["stolen_base_average"], batter["triples"],
		batter["ops"], batter["singles"], batter["stolen_bases"], batter["runs"], batter["plate_appearances_per_rbi"], batter["doubles"],
		batter["plate_appearances"], batter["at_bats_per_home_run"], batter["obp_string"], batter["hits"], batter["at_bats_per_rbi"],
		batter["strikeout_rate"], batter["sacrifices"], batter["walk_rate"], batter["rbi"], batter["strike_outs"], batter["slg"], batter["obp"]))
	home_batters = cur.lastrowid

	#individual batters
	batter = output["home_batters"]
	batterId = []
	for b in batter:
		cur.execute("insert into fantasy_batter (sac_hits, slg_string, last_name, rbi_with_two_outs, batting_highlights, sub_batting_order, "
			+"sac_flies, total_bases, caught_stealing, team_abbreviation, hit_by_pitch, home_runs, avg_string, avg, extra_base_hits," +
			" first_name, display_name, at_bats, left_on_base, plate_appearances_per_home_run, walks, ops_string, " +
			"stolen_base_average, bat_order, triples, ops, singles, stolen_bases, runs, plate_appearances_per_rbi, position, "+
			"plate_appearances, at_bats_per_home_run, obp_string, hits, at_bats_per_rbi, strike_outs, strikeout_rate, sacrifices, "+
			"walk_rate, rbi, doubles, slg, obp) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " +
			"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
			(b["sac_hits"], b["slg_string"], b["last_name"], b["rbi_with_two_outs"], b["batting_highlights"], b["sub_bat_order"],
			b["sac_flies"], b["total_bases"], b["caught_stealing"], b["team_abbreviation"], b["hit_by_pitch"], b["home_runs"],
			b["avg_string"], b["avg"], b["extra_base_hits"], b["first_name"], b["display_name"], b["at_bats"], b["left_on_base"],
			b["plate_appearances_per_home_run"], b["walks"], b["ops_string"], b["stolen_base_average"], b["bat_order"],
			b["triples"], b["ops"], b["singles"], b["stolen_bases"], b["runs"], b["plate_appearances_per_rbi"], b["position"],
			b["plate_appearances"], b["at_bats_per_home_run"], b["obp_string"], b["hits"], b["at_bats_per_rbi"], b["strike_outs"],
			b["strikeout_rate"], b["sacrifices"], b["walk_rate"], b["rbi"], b["doubles"], b["slg"], b["obp"]))
		batterId.append(cur.lastrowid)

	batter = output["away_batters"]
	for b in batter:
	     	cur.execute("insert into fantasy_batter (sac_hits, slg_string, last_name, rbi_with_two_outs, batting_highlights, sub_batting_order," +
	     		" sac_flies, total_bases, caught_stealing, team_abbreviation, hit_by_pitch, home_runs, avg_string, avg, extra_base_hits, " +
	     		"first_name, display_name, at_bats, left_on_base, plate_appearances_per_home_run, walks, ops_string, " +
	     		"stolen_base_average, bat_order, triples, ops, singles, stolen_bases, runs, plate_appearances_per_rbi, position, " +
	     		"plate_appearances, at_bats_per_home_run, obp_string, hits, at_bats_per_rbi, strike_outs, strikeout_rate, sacrifices, " +
	     		"walk_rate, rbi, doubles, slg, obp) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " +
	     		"%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
	     		(b["sac_hits"], b["slg_string"], b["last_name"], b["rbi_with_two_outs"], b["batting_highlights"], b["sub_bat_order"],
     			b["sac_flies"], b["total_bases"], b["caught_stealing"], b["team_abbreviation"], b["hit_by_pitch"], b["home_runs"],
     			b["avg_string"], b["avg"], b["extra_base_hits"], b["first_name"], b["display_name"], b["at_bats"], b["left_on_base"],
     			b["plate_appearances_per_home_run"], b["walks"], b["ops_string"], b["stolen_base_average"], b["bat_order"],
     			b["triples"], b["ops"], b["singles"], b["stolen_bases"], b["runs"], b["plate_appearances_per_rbi"], b["position"],
     			b["plate_appearances"], b["at_bats_per_home_run"], b["obp_string"], b["hits"], b["at_bats_per_rbi"], b["strike_outs"],
     			b["strikeout_rate"], b["sacrifices"], b["walk_rate"], b["rbi"], b["doubles"], b["slg"], b["obp"]))
 		batterId.append(cur.lastrowid)

	#start_date_time, attendence, temperature, season_type
	temp = output["event_information"]
	site = cur.execute("select id from fantasy_site where name='" + temp["site"]["name"] + "'")
	site = cur.fetchone()[0]
	cur.execute("insert into fantasy_scoreboard (home_fantasy_team_id, away_fantasy_team_id, away_batters_total_id, home_batters_total_id,"
		+" home_period_scores, away_period_scores, start_date_time, attendance, temperature, season_type, fantasy_site_id) values "+
		"(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (home, away, away_batters, home_batters, str(output["home_period_scores"]),
		str(output["away_period_scores"]), temp["start_date_time"], temp["attendance"], temp["temperature"], temp["season_type"], site))
	scoreboard = cur.lastrowid

	for p in pitchersId:
		cur.execute("insert into fantasy_scoreboard_to_pitcher (scoreboard_id, pitcher_id) values (%s, %s)", (scoreboard, p))

	for p in batterId:
		cur.execute("insert into fantasy_scoreboard_to_batter (scoreboard_id, batter_id) values (%s, %s)", (scoreboard, p))
	con.commit()

	#ignoring officials
	fantasy_scoreboard(cur, temp["start_date_time"][:10], scoreboard, home, away)


	con.commit()
	con.close()

def league_games(cur, date):

	cur.execute("select id from fantasy_league")

	for league in cur.fetchall():
		#select a game to use
		cur.execute('select id from fantasy_game where date = %s', date)
		game = cur.fetchone()[0]
		#insert into the selected
		cur.execute('insert into fantasy_league_game (date, game_id) values (%s, %s)', (date, game))
		fantasy_league_game_id = cur.lastrowid
		#if monday insert into league_games otherwise update league_games
		dayOfWeek = datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])).isoweekday()

		if dayOfWeek == 1: #Monday
			cur.execute('insert into fantasy_league_games (league_id, start_date, monday_id) values ' +
				'(%s, %s, %s)', (league[0], date, fantasy_league_game_id))

		elif dayOfWeek == 2: #Tuesday
			tuesday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-1)).strftime("%Y%m%d")
			print 
			cur.execute('update fantasy_league_games set tuesday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], tuesday))

		elif dayOfWeek == 3: #Wednesday
			wednesday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-2)).strftime("%Y%m%d")
			cur.execute('update fantasy_league_games set wednesday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], wednesday))

		elif dayOfWeek == 4: #Thursday
			thursday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-3)).strftime("%Y%m%d")
			cur.execute('update fantasy_league_games set thursday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], thursday))

		elif dayOfWeek == 5: #Friday
			friday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-4)).strftime("%Y%m%d")
			cur.execute('update fantasy_league_games set friday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], friday))

		elif dayOfWeek == 6: #Saturday
			saturday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-5)).strftime("%Y%m%d")
			cur.execute('update fantasy_league_games set saturday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], saturday))

		elif dayOfWeek == 7: #Sunday
			sunday = (datetime.date(int(date[:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=-6)).strftime("%Y%m%d")
			cur.execute('update fantasy_league_games set sunday_id = %s where league_id = %s and start_date = %s',
				(fantasy_league_game_id, league[0], sunday))


def fantasy_scoreboard(cur, date, scoreboard_id, home_team_id, away_team_id):
	
	#dayOfWeek = datetime.date(int(date[:4]), int(date[5:7]), int(date[8:10])).isoweekday() #gets the day of week
	
	#gets the start of week date for searching
	#start_date = (datetime.date.today() + datetime.timedelta(days=-(7 - dayOfWeek - 1)))
	
	temp_date = date[:4] + date[5:7] + date[8:10]
	
	game = cur.execute('select id from fantasy_game where date = %s and home_id = %s and away_id = %s',
		(temp_date, home_team_id, away_team_id))
	game = cur.fetchone()[0]

	temp_date = date + "%"
	print temp_date, home_team_id, away_team_id
	scoreboard = cur.execute('select id from fantasy_scoreboard ' +
		'where start_date_time like %s and home_fantasy_team_id = %s and away_fantasy_team_id = %s',
		(temp_date, home_team_id, away_team_id))
	scoreboard = cur.fetchone()[0]

	temp_date = date[:4] + date[5:7] + date[8:10]
	print scoreboard, temp_date, game

	#the league names
	leagues_game = cur.execute("update fantasy_league_game set scoreboard_id = %s where date = %s and game_id = %s",
		(scoreboard, temp_date, game))
