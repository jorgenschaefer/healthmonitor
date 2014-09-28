from django.db import models
from django.contrib.auth.models import User


class Weight(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    weight = models.FloatField()

    class Meta:
        unique_together = [("user", "date")]

    def __str__(self):
        return "{} at {} kg on {}".format(self.user.username,
                                          self.weight,
                                          self.date)
