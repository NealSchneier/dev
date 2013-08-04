from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from models import Team, Scoreboard, Game, League, League_Games, League_Game, picks
from django.contrib.auth.models import User

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

def league(request, offset):
    #leage details
    template = get_template('league.html')
    league = League.objects.filter(id=offset)[:1].get()
    html = template.render(Context({'league': league}))
    return HttpResponse(html)

def league_weekly(request, offset):
    #a league's weekly games
    template = get_template('weekly.html')
    league_weekly = League_Games.objects.select_related().get(id=offset)
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
    template = get_template('index.html')

    html = template.render(Context())
    return HttpResponse(html)