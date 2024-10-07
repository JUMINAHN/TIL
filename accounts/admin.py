from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #auth와 관련됨
from .models import User


# Register your models here.
# admin사이트에 등록을 해야함
# 무엇을 ? User와 그 user를 재정의한 관리자를 
admin.site.register(User, UserAdmin)