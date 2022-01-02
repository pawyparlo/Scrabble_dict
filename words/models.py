from django.db import models
from django.db.models.aggregates import Max

class Letters(models.Model):
    letters = models.CharField(max_length=7)



