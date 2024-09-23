from django.db import models
from django.utils.timezone import localtime

# Create your models here.
class Garage(models.Model):
    #여는시간과 닫는 시간은 timefield를 사용
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField(Event())
    closing_time = models.TimeField(Event())


class Event(models.Model):
    start_time = models.DateTimeField()

    def get_local_start_time(self):
        return localtime(self.start_time)