from django.db import models
#settings에 접근해야 함
from django.conf import settings

# Create your models here.
# N:1관계 만들기
class Book(models.Model): #Book과 - Review가 1:N
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    

#review의 foreginkey가 -> book이 될 것 (1대 N관계를 생각해보면)
class Review(models.Model): #user와 - Review가 1:N 관계
    user = models.ForeignKey(Book, on_delete=models.CASCADE)
    book = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)

## 각각의 관계 설정
# user모델과 -> 상기 모델 두개 모두 관리할 수 있어야 함