from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin) #user와 useradmin에 대한 내용을 등록해주겠습니다. == setting 완료