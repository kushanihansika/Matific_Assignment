from django.db import models


class Tounament(models.Model):
    name = models.CharField(max_length=255, default="")
