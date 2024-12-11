from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Customer(models.Model): #고객이 제품을 사는 것으로
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ManyToManyField(Product) #proudct field와 M:N 관계 맺기 -> 동등하게