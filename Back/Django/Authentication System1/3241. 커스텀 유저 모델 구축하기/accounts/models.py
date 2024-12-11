from django.db import models
#원래 db에 만들 model 생성했었음
#이제는 User model을 다시 새롭게 갱신
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass #이렇게 생성을 하고
