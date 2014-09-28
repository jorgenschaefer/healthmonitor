from django.db import models
from django.contrib.auth.models import User


class Weight(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    weight = models.FloatField()
