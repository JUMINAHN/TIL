from django.db import models
from django.contrib.auth.models import AbstractUser #model에 있는 내용  
#상위 User -> abstractuser 받아야함 :: login page 다시 학습 필요

# Create your models here.
class User(AbstractUser): #user 아마 기존 -> 일단은 주어진 조건에 맞게만 수행을 한다.
    pass