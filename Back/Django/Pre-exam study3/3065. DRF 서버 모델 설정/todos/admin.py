from django.contrib import admin
from .models import Todo

# Register your models here.
# todo data를 관리자 계정에서 확인할 수 있도록
admin.site.register(Todo)