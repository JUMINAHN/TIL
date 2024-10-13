from django.db import models

# Create your models here.
class Accounts(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)