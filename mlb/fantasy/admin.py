from django.contrib import admin
from fantasy.models import Game,Pitcher, Batter_Totals, Batter, Scoreboard, League, Team, Site, Surface, League_Games

admin.site.register(Game)
admin.site.register(Pitcher)
admin.site.register(Batter_Totals)
admin.site.register(Batter)
admin.site.register(Scoreboard)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Site)
admin.site.register(Surface)
admin.site.register(League_Games)

