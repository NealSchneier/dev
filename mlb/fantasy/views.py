from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.loader import get_template
from models import Team, Scoreboard, Game, League, League_Games, League_Game, picks, User, Batter_Points, Pitcher_Points
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import datetime

def teams(request):
    template = get_template('teams.html')
    teams = Team.objects.all()
    html = template.render(Context({'teams': teams}))
    return HttpResponse(html)

def scoreboards(request, offset):
    #scores from the game

    date = offset [:4] + "-" + offset[4:6] + "-" + offset[6:8] + "%"

    template = get_template('scoreboards.html')
    scoreboards = Scoreboard.objects.raw('select scoreboard.id,  t1.full_name home, t2.full_name away '
        + 'from fantasy_scoreboard scoreboard join fantasy_team t1 on (scoreboard.home_fantasy_team_id '
        + '= t1.id ) join fantasy_team t2 on (scoreboard.away_fantasy_team_id = t2.id) '
        +'where scoreboard.start_date_time LIKE %s order by scoreboard.start_date_time',  date)

    html = template.render(Context({'scoreboards': scoreboards}))
    return HttpResponse(html)

def scoreboards_recent(request):
    #redirects with current date
    return redirect("scoreboards_date", datetime.date.today().strftime("%Y%m%d"))


def league(request, offset):
    #leage details
    #check if user is logged in
    if not request.user.is_authenticated() :
        return redirect("/temp")
    #check if user is in the current league
    template = get_template('league.html')
    league = League.objects.filter(id=offset)[:1].get()
    html = template.render(Context({'league': league}))
    return HttpResponse(html)

def league_weekly(request, league, start_date):
    if not request.user.is_authenticated():
        return redirect("/temp")
    #a league's weekly games
    template = get_template('weekly.html')
    league_weekly = League_Games.objects.select_related().get(league=league, start_date=start_date)
    html = template.render(Context({'weekly':league_weekly}))
    return HttpResponse(html)

def game(request, offset):
    # specific game details - before the game
    try:
        offset = str(offset)
    except ValueError:
        raise Http404()
    template = get_template('game.html')
    monday = Game.objects.filter(date=offset)[:1].get()
    html = template.render(Context({'monday': monday}))
    return HttpResponse(html)

def games(request, offset):
    try:
        offset = str(offset)
    except ValueError:
        raise Http404()
    template = get_template('games.html')
    monday = Game.objects.filter(date=offset)[:1].get()
    html = template.render(Context({'monday': monday}))
    return HttpResponse(html)

#form to create user
def add_user(request):
    #when the user has selected the form
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(user, email, password)
        user.is_staff = False
        user.save()
        return redirect("/temp")

    html = render_to_response('user.html', None, RequestContext(request))
    return HttpResponse(html)


#form to create user
def add_league(request):
    #when the user has selected the form
    if request.method == 'POST':
        name = request.POST['name']
        league = League.objects.create()
        league.active = "Y"
        league.name = name
        league.save()
        return redirect("/temp")

    html = render_to_response('addLeague.html', None, RequestContext(request))
    return HttpResponse(html)

#form for the daily picks
def daily_picks(request, user, date):

    if request.method == 'POST':


        picks = Picks.objects.create()


    return HttpResponse("")

#form for the weekly picks
def weekly_picks(request, user, date):


    return HttpResponse("")

def temp(request):

    if request.method == 'POST':
            user = login_view(request)
            if user is None:
                return redirect('/teams')
            else:
                login(request, user)
                authenticate_league(user)
    html = render_to_response('index.html', None, RequestContext(request))
    return HttpResponse(html)

def logout_view(request):
    logout(request)
    return redirect('/temp')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return user

def authenticate_league(User):
    league_data = League.objects.raw('select * from fantasy_league where active="Y" and (user1_id=%s or user2_id=%s or user3_id=%s or user4_id=%s or user5_id=%s or user6_id=%s or user7_id=%s or user8_id=%s or user9_id=%s or user10_id=%s or user11_id=%s or user12_id=%s )',  (User.id, User.id, User.id, User.id, User.id, User.id, User.id, User.id, User.id, User.id, User.id, User.id))
    return league_data

def is_league_authenticated():
    print
    #this would be used similar to is_authenticated

def scoring_and_settings(request, league):
    #add authentication to for both user and determine
    print

def leaguedirectory(request):
    template = get_template('leaguedirectory.html')
    league = League.objects.select_related()
    html = template.render(Context({'leagues':league}))
    return HttpResponse(html)

def leaguedetails(request, offset):
    #add form so that the details can be edited
    template = get_template('leaguedetails.html')
    league = League.objects.select_related().get(id=offset)
    html = template.render(Context({'league':league}))
    return HttpResponse(html)

def leaguescoring(request, offset):
    #add form so that the details can be edited

    if request.method == 'GET':
        template = get_template('leaguescoring.html')
        batter_points = Batter_Points.objects.select_related().get(league=offset)
        pitcher_points = Pitcher_Points.objects.select_related().get(league=offset)
        html = template.render(Context({'batter_points':batter_points, 'pitcher_points':pitcher_points}))
    elif request.method == 'POST':
        #batter points
        gp = request.POST['gp']

        #pitcher points
        app = request.POST['app']
    return HttpResponse(html)

