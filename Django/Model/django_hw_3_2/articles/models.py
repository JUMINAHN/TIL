from django.db import models

# Create your models here.
# 상품 정보 data를 담을 데이터를 생성한다.
class Article(models.Model): #model은 class를 만든다.
    title = models.CharField(max_length=15)
    content = models.TextField()