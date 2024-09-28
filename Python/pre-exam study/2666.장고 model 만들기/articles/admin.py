from django.contrib import admin
from .models import Article
# Register your models here.
# 관리자 계정을 사용할 수 있도록 해야한다.
# 내가 등록한 모델을 사용하기 위해선 호출해야 함
admin.site.register(Article) #관리자 사이트 등록 -> 으로 이해하면 된다.

#admin을 하기 위해선 -> migrate를 해줘야함