from django.db import models

# Create your models here.
class Todo(models.Model): #부모
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

#추천-> 자식?
class Recommend(models.Model):  #todo와 Recommend는 1:N관계
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()