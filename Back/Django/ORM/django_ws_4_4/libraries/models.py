from django.db import models

# Create your models here.
class Book(models.Model) :
    Title = models.CharField(max_length=50) #문자 => 문자열로 들어가기
    author = models.CharField(max_length=15)
    pubdate = models.DateField() #날짜 -> timezone.value
    startIndex = models.IntegerField() #page수 == 숫자가 들어가야 한다. == 기본값 
    pricesales = models.IntegerField() #가격
    adult = models.BooleanField() #성인 등급 여부
    ISBN = models.IntegerField()
    customerReviewRank = models.IntegerField()
    #isbn과 제목, 발행일자
    #8개