from django.db import models

# 데이터 조작은 직접 shell을 통해서 진행
# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()