from django.db import models
from tournament.models import Tounament
from team.models import Team
from user.models import User


class Matces(models.Model):
    match_name = models.CharField(max_length=255, default="")
    venue = models.CharField(max_length=25, default="")
    team = models.ManyToManyField(Team, through='MatcesTeamDetails')
    user = models.ManyToManyField(User, through='MatcesUserDetails')
    tournament = models.ForeignKey(
        Tounament, on_delete=models.CASCADE, null=True)


class MatcesTeamDetails(models.Model):
    match = models.ForeignKey(Matces, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_score = models.IntegerField(default=0)

    class Meta:
        unique_together = [['team', 'match']]


class MatcesUserDetails(models.Model):
    match = models.ForeignKey(Matces, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_score = models.IntegerField(default=0)
