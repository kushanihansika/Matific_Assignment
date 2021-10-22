
from django.db import models
from team.models import Team
from role.models import Role


class User(models.Model):
    user_name = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=25, default="")
    email = models.EmailField
    team = models.ForeignKey(
        Team, null=True, on_delete=models.SET_NULL, related_name='users')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
