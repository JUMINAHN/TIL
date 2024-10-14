# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    #1대 N관계 형성
    #추가로 M:N관계 형성
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #또 user와 article의 관계 -> 참조할 것 -> 아티클과 어떠한 것의 관계를 맺을것인가?
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_user") #좋아요를 위해서 -> like_user로 바꾼다
    #또 똑같은 필드를 참조해서 user.article_set.all()이 되고있는 상황이었음
    #별도 중개모델 없이 장고 내장시스템에서 가능하다
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)