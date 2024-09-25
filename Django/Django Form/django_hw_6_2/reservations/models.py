from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=10) #여기서 이미 받기로 함
    date = models.DateField()