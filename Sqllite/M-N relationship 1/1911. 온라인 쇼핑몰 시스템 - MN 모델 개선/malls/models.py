from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ManyToManyField('Product')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# M : N 관계
# M : N 관계이지만 -> foreignkey로 작성
class Order(models.Model): #reservation을 이번에 orderModel로 정의
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_customer")
    quantity = models.IntegerField()
    order_date = models.DateField()
    