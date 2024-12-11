from django.contrib import admin
from .models import Article #aritcle을 등록해야함

# Register your models here.
# model article을 등록을 해야한다.

# 관리자 사이트에 등록한다 -> 저거를
admin.site.register(Article)