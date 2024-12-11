from django.db import models
from django.contrib.auth.models import AbstractUser #auth인증과 관련됨 -> django의 contrib에 있음 
# Create your models here.
# User model을 재정의해야 사용할 수 있다 -> 그러기 위해선 AbstractUser를 사용해야 함
class User(AbstractUser):
    pass #AbstractUser를 상속받아야 사용할 수 있음 