from django.contrib import admin
from .models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display = ('__str__','match_date', 'kick_off', 'home_score', 'visiting_score', 'match_status')

admin.site.register(Match, MatchAdmin)
