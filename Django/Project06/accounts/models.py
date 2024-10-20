from django.db import models
from django.contrib.auth.models import AbstractUser


#following 기능을 구현하기 위해서는 재귀적 구저 User과 User간의 진행
class User(AbstractUser):
    nickname = models.CharField(max_length=30)
    #역참조시 == followers로 하도록 설정하는 것
    #유저끼리의 참조를 확인하는 것
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers') #나 자신을 참조하되, 비대칭
