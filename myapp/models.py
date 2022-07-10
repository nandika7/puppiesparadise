from django.db import models

class Dates(models.Model):
    date = models.DateField()
    days = models.IntegerField()
# Create your models here.
