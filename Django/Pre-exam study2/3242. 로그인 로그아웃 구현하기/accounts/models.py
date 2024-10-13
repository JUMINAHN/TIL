from django.db import models
#usermodel 상속 -> abstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
