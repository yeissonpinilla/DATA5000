from django.db import models

# Create your models here.
class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    #competition_id, will be added when there is a competition app.
    country_name = models.TextField(max_length=35)
    #season will be added when there is a season app.
    match_date = models.DateField()
    kick_off = models.TimeField()
    #stadium will be added when there is an stadium app.
    home_team_gender = models.TextField(max_length=10)
    #team app needed
    home_score = models.IntegerField()
    visiting_score = models.IntegerField()
    match_status = models.TextField(max_length=20)
    