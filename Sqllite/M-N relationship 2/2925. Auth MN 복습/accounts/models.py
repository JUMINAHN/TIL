from django.db import models
from django.contrib.auth.models import AbstractUser

#user로 관계형성
#M과 N의 관계 형성
class User(AbstractUser):
    #user 관계
    #유저의 입장에서 -> 다른 사람과의 관계를 맺는것 : 나의 입장에서 팔로잉
    #자기자신을 참조하는 것 -> many to many 에서 self로 해야하기 때문에 user로 적는것안됨
    #다만 symmetrical = False로 설정하기
    following = models.ManyToManyField('self', symmetrical=False, related_name="followers")
    #타인의 입장에서 나는 팔로워