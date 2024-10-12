
from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name="index"), #view -> 접근
    #상세 정보에 접근해야 합니다.
    path('<int:author_pk>', views.detail, name="detail"), #url 링크가 author_pk인 것
]
