from django.db import models

class UserInfo(models.Model):
    userId = models.BigIntegerField(blank=False)
    userName = models.CharField(max_length=200, blank=False)
    userTemperature = models.FloatField(blank=False)
    measuredDatetime = models.DateTimeField(auto_now_add=True, primary_key=True)
    measuredPlace = models.CharField(max_length=200, blank=False)
