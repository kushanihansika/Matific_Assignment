from django.db import models
from django.db.models.deletion import SET, SET_NULL


class Team(models.Model):
    team_name = models.CharField(max_length=255)


# class Role(models.Model):
#     role_name = models.CharField(max_length=255, default="")


# class User(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     password = models.CharField(max_length=25, default="")
#     team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
