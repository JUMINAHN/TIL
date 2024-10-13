from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
#admin site 등록

# Register your models here.
admin.site.register(User, UserAdmin) #이거는 예외
