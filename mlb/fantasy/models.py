from django.db import models
from django.contrib.auth.models import User

#These models are from the requests from XMLStats
class Team(models.Model):
	conference = models.CharField(max_length=100)
	division = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	site_name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=100)
	team_id = models.CharField(max_length=100)
	full_name = models.CharField(max_length=100)
	active = models.CharField(max_length=10)

	def __unicode__(self):
		return self.full_name

class Surface(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Site(models.Model):
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	capacity = models.IntegerField()
	name = models.CharField(max_length=100)
	surface = models.ForeignKey(Surface)

	def __unicode__(self):
		return self.name

class Game(models.Model):
	event_id = models.CharField(max_length=100)
	season_type = models.CharField(max_length=100)
	site = models.ForeignKey(Site)
	away = models.ForeignKey(Team, related_name='+')
	home = models.ForeignKey(Team, related_name='+')
	event_status = models.CharField(max_length=100)
	sport = models.CharField(max_length=100)
	date = models.CharField(max_length=10)

	def __unicode__(self):
		return self.away.full_name + " at " + self.home.full_name + " - " + self.date

class Pitcher(models.Model):
	last_name = models.CharField(max_length=100)
	win = models.CharField(max_length=5)
	runs_allowed = models.IntegerField()
	hit_by_pitch = models.IntegerField()
	walks  = models.IntegerField()
	intentional_walks  = models.IntegerField()
	whip  = models.IntegerField()
	first_name  = models.CharField(max_length=100)
	errors  = models.IntegerField()
	display_name  = models.CharField(max_length=100)
	pitches_strikes  = models.IntegerField()
	innings_pitched = models.DecimalField(max_digits=5, decimal_places=1)
	save  = models.CharField(max_length=100)
	era = models.DecimalField(max_digits=5, decimal_places=2)
	home_runs_allowed  = models.IntegerField()
	pitch_order  = models.IntegerField()
	hits_allowed  = models.IntegerField()
	wild_pitches  = models.IntegerField()
	loss  = models.CharField(max_length=5)
	earned_runs  = models.IntegerField()
	team_abbreviation  = models.ForeignKey(Team)
	pitch_count  = models.IntegerField()
	strike_outs  = models.IntegerField()

	def __unicode__(self):
		return self.display_name


class Batter_Totals(models.Model):
	sac_hits = models.IntegerField()
	slg_string   = models.CharField(max_length=10)
	rbi_with_two_outs = models.IntegerField()
	batting_highlights   = models.CharField(max_length=200)
	sac_flies = models.IntegerField()
	total_bases = models.IntegerField()
	avg_string   = models.CharField(max_length=10)
	avg = models.DecimalField(max_digits=8, decimal_places=3)
	extra_base_hits = models.IntegerField()
	at_bats = models.IntegerField()
	left_on_base = models.IntegerField()
	plate_appearances_per_home_run = models.DecimalField(max_digits=8, decimal_places=3)
	walks = models.IntegerField()
	ops_string   = models.CharField(max_length=10)
	stolen_base_average = models.DecimalField(max_digits=8, decimal_places= 3)
	triples = models.IntegerField()
	ops = models.DecimalField(max_digits=8, decimal_places=3)
	singles  = models.IntegerField()
	stolen_bases  = models.IntegerField()
	runs  = models.IntegerField()
	caught_stealing  = models.IntegerField()
	plate_appearances_per_rbi = models.DecimalField(max_digits=8, decimal_places=3)
	doubles = models.IntegerField()
	plate_appearances  = models.IntegerField()
	at_bats_per_home_run = models.DecimalField(max_digits=8, decimal_places=3)
	obp_string  = models.CharField(max_length=10)
	hits  = models.IntegerField()
	at_bats_per_rbi = models.DecimalField(max_digits=8, decimal_places=3)
	strikeout_rate = models.DecimalField(max_digits=8, decimal_places=3)
	sacrifices  = models.IntegerField()
	home_runs  = models.IntegerField()
	walk_rate = models.DecimalField(max_digits=8, decimal_places=3)
	rbi  = models.IntegerField()
	hit_by_pitch  = models.IntegerField()
	strike_outs  = models.IntegerField()
	slg = models.DecimalField(max_digits=8, decimal_places=3)
	obp = models.DecimalField(max_digits=8, decimal_places=3)


class Batter(models.Model):
	sac_hits  = models.IntegerField()
	slg_string  = models.CharField(max_length=10)
	last_name  = models.CharField(max_length=100)
	rbi_with_two_outs  = models.IntegerField()
	batting_highlights  = models.CharField(max_length=100)
	sub_batting_order  = models.IntegerField()
	sac_flies  = models.IntegerField()
	total_bases  = models.IntegerField()
	caught_stealing  = models.IntegerField()
	team_abbreviation  = models.CharField(max_length=100)
	hit_by_pitch  = models.IntegerField()
	home_runs  = models.IntegerField()
	avg_string  = models.CharField(max_length=10)
	avg = models.DecimalField(max_digits=8, decimal_places=3)
	extra_base_hits  = models.IntegerField()
	first_name  = models.CharField(max_length=100)
	display_name  = models.CharField(max_length=100)
	at_bats  = models.IntegerField()
	left_on_base  = models.IntegerField()
	plate_appearances_per_home_run = models.DecimalField(max_digits=8, decimal_places=3)
	walks  = models.IntegerField()
	ops_string  = models.CharField(max_length=10)
	stolen_base_average = models.DecimalField(max_digits=8, decimal_places=3)
	bat_order  = models.IntegerField()
	triples  = models.IntegerField()
	ops = models.DecimalField(max_digits=8, decimal_places=3)
	singles  = models.IntegerField()
	stolen_bases  = models.IntegerField()
	runs  = models.IntegerField()
	plate_appearances_per_rbi = models.DecimalField(max_digits=8,  decimal_places=3)
	position  = models.CharField(max_length=10)
	plate_appearances  = models.IntegerField()
	at_bats_per_home_run = models.DecimalField(max_digits=8, decimal_places=3)
	obp_string  = models.CharField(max_length=10)
	hits  = models.IntegerField()
	at_bats_per_rbi = models.DecimalField(max_digits=8, decimal_places=3)
	strike_outs  = models.IntegerField()
	strikeout_rate = models.DecimalField(max_digits=8, decimal_places=3)
	sacrifices  = models.IntegerField()
	walk_rate = models.DecimalField(max_digits=8, decimal_places=3)
	rbi  = models.IntegerField()
	doubles  = models.IntegerField()
	slg = models.DecimalField(max_digits=8, decimal_places=3)
	obp = models.DecimalField(max_digits=8, decimal_places=3)

	def __unicode__(self):
		return self.display_name + " - " + self.batting_highlights

class Official(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.last_name + ", "+self.first_name


class Officials(models.Model):
	home  = models.ForeignKey(Official, related_name='+')
	first  = models.ForeignKey(Official, related_name='+')
	second  = models.ForeignKey(Official, related_name='+')
	third  = models.ForeignKey(Official, related_name='+')

	def __unicode__(self):
		return self.home.last_name + ", "+ self.first.last_name + ", "+ self.second.last_name + ", and "+ self.third.last_name

class Scoreboard(models.Model):
	home_fantasy_team  = models.ForeignKey(Team, related_name='+')
	away_fantasy_team  = models.ForeignKey(Team, related_name='+')
	away_batters_total   = models.ForeignKey(Batter_Totals, related_name='+')
	home_batters_total   = models.ForeignKey(Batter_Totals, related_name='+')
	home_period_scores = models.CharField(max_length=100)
	away_period_scores = models.CharField(max_length=100)
	officials  = models.ForeignKey(Officials, blank=True, null=True)
	start_date_time = models.CharField(max_length=100)
	attendance = models.IntegerField()
	temperature = models.DecimalField(max_digits=5, decimal_places=2)
	season_type = models.CharField(max_length=100)
	fantasy_site = models.ForeignKey(Site)

	def __unicode__(self):
		return self.away_fantasy_team.full_name + " at "+ self.home_fantasy_team.full_name +" - "+ self.start_date_time

class Scoreboard_To_Pitcher(models.Model):
	scoreboard  = models.ForeignKey(Scoreboard)
	pitcher   = models.ForeignKey(Pitcher)

class Scoreboard_To_Batter(models.Model):
	scoreboard  = models.ForeignKey(Scoreboard)
	batter   = models.ForeignKey(Batter)

#these are the tables for the system

class League(models.Model):
	name = models.CharField(max_length=20)
	user1 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user2 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user3 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user4 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user5 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user6 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user7 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user8 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user9 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user10 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user11 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	user12 = models.ForeignKey(User, blank=True, null=True, related_name='+')
	active = models.CharField(max_length=1)

	def __unicode__(self):
		return self.name

	@classmethod
	def create(cls, name):
		league = cls(name=name)
		league.active = "Y"
		return league

class League_Game(models.Model):
	date = models.CharField(max_length=10)
	game = models.ForeignKey(Game)
	scoreboard = models.ForeignKey(Scoreboard, blank=True, null=True)


class League_Games(models.Model):
	league = models.ForeignKey(League)
	start_date = models.CharField(max_length=10)
	monday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	tuesday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	wednesday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	thursday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	friday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	saturday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')
	sunday = models.ForeignKey(League_Game, blank=True, null=True, related_name='+')

	def __unicode__(self):
		return self.league.name + " starts "+ self.start_date + " " + self.monday.game.event_id




#the point system for batters - relates to each league
class Batter_Points(models.Model):
	league = models.ForeignKey(League)
	gp = models.IntegerField()
	gs = models.IntegerField()
	avg = models.DecimalField(max_digits=8, decimal_places=3)
	obp = models.DecimalField(max_digits=8, decimal_places=3)
	slg = models.DecimalField(max_digits=8, decimal_places=3)
	ab = models.IntegerField()
	r = models.IntegerField()
	h = models.IntegerField()
	singles = models.IntegerField()
	doubles = models.IntegerField()
	triples = models.IntegerField()
	hr =  models.IntegerField()
	rbi = models.IntegerField()
	sh = models.IntegerField()
	sf = models.IntegerField()
	sb= models.IntegerField()
	cs = models.IntegerField()
	bb = models.IntegerField()
	ibb = models.IntegerField()
	hbp = models.IntegerField()
	k = models.IntegerField()
	gidp = models.IntegerField()
	ops = models.DecimalField(max_digits=8, decimal_places=3)
	tb =  models.IntegerField()
	po =  models.IntegerField()
	a =  models.IntegerField()
	e =  models.IntegerField()
	fpct = models.DecimalField(max_digits=8, decimal_places=3)
	xbh =  models.IntegerField()
	nsb  =  models.IntegerField()
	sb_percentage = models.DecimalField(max_digits=8, decimal_places=3)
	cyc =  models.IntegerField()
	pa  =  models.IntegerField()
	slam =  models.IntegerField()
	ofa =  models.IntegerField()
	dpt =  models.IntegerField()
	ci =  models.IntegerField()


#the point system for pitchers - relates to each league
class Pitcher_Points(models.Model):
	league = models.ForeignKey(League)
	app =  models.IntegerField()
	gs =  models.IntegerField()
	era = models.DecimalField(max_digits=8, decimal_places=3)
	whip = models.DecimalField(max_digits=8, decimal_places=3)
	wins =  models.IntegerField()
	losses =  models.IntegerField()
	cg =  models.IntegerField()
	sho =  models.IntegerField()
	sv =  models.IntegerField()
	out =  models.IntegerField()
	h =  models.IntegerField()
	tbf =  models.IntegerField()
	r =  models.IntegerField()
	er =  models.IntegerField()
	hr =  models.IntegerField()
	bb =  models.IntegerField()
	ibb =  models.IntegerField()
	hbp =  models.IntegerField()
	k =  models.IntegerField()
	wp =  models.IntegerField()
	blk =  models.IntegerField()
	sb =  models.IntegerField()
	gidp =  models.IntegerField()
	svop =  models.IntegerField()
	hld =  models.IntegerField()
	k_per_nine = models.DecimalField(max_digits=8, decimal_places=3)
	k_per_walks = models.DecimalField(max_digits=8, decimal_places=3)
	tb =  models.IntegerField()
	ip = models.DecimalField(max_digits=8, decimal_places=3)
	pc =  models.IntegerField()
	singles =  models.IntegerField()
	doubles =  models.IntegerField()
	triples =  models.IntegerField()
	rw =  models.IntegerField()
	rl =  models.IntegerField()
	pick =  models.IntegerField()
	rapp =  models.IntegerField()
	obpa  = models.DecimalField(max_digits=8, decimal_places=3)
	win_percentage = models.DecimalField(max_digits=8, decimal_places=3)
	hits_per_nine = models.DecimalField(max_digits=8, decimal_places=3)
	walks_per_nine = models.DecimalField(max_digits=8, decimal_places=3)
	nh =  models.IntegerField()
	pg =  models.IntegerField()
	save_percentage = models.DecimalField(max_digits=8, decimal_places=3)
	ira =  models.IntegerField()
	qs =  models.IntegerField()
	bsv =  models.IntegerField()
	nsv =  models.IntegerField()



#the picked winner for each game for each player
class picks(models.Model):
	user = models.ForeignKey(User)
	league_game = models.ForeignKey(League_Game)
	winner = models.ForeignKey(Team)


