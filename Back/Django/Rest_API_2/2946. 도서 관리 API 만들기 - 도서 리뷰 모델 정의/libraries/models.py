from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.TextField(max_length=10)
    author = models.TextField()
    title = models.TextField()

#book과 review는 1:N관계를 가진다.
class Review(models.Model): #하나의 book을 연결
    #N을 기준으로 외래키 설정 
    book = models.ForeignKey(Book, on_delete=models.CASCADE) #외래키 연결 
    content = models.TextField()
    score = models.IntegerField() #field
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
