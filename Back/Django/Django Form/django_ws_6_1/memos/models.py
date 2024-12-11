from django.db import models

# Create your models here.
# model에서는 class를 생성한다.
class Memos(models.Model):
    summary = models.CharField(max_length=20)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
