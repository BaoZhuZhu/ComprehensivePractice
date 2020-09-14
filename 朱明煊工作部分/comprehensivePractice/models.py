from django.db import models

class UserInfo(models.Model):
    userId = models.BigIntegerField(blank=False)
    userName = models.CharField(max_length=200, blank=False)
    userTemperature = models.FloatField(blank=False)
    measuredDatetime = models.DateTimeField(primary_key=True)
    measuredPlace = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "uid: " + str(self.userId) + "\n" \
               + "name: " + str(self.userName) + "\n" \
               + "temp: " + str(self.userTemperature) + "\n"\
               + "dtm: " + str(self.measuredDatetime) + "\n" \
               + "place: " + str(self.measuredPlace)
