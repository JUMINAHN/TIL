from django.db import models

# Create your models here.
class Book(models.Model): #부모 1
    isbn = models.TextField(max_length=10)
    author = models.TextField()
    title = models.TextField()

#자식 N => 게시글 한개에 댓글 여러개 
class Review(models.Model): #book과 모델은 1:N관계를 가진다
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)