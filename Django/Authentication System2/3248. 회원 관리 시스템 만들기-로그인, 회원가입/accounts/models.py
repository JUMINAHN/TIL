from django.db import models
from django.contrib.auth.models import AbstractUser #user와 관련된 모델을 불러와야하기 떄문에


# user모델 재정의 -> user 자체는 인증과 관련됨
# Create your models here.
class User(AbstractUser):
    pass