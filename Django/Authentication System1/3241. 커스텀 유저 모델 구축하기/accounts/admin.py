from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# 관리자 사이트에서 사용할 User -> 그리고 그것을 UserAdmin에서도 사용을 해야함
admin.site.register(User, UserAdmin)