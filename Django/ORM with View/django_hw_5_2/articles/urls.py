from django.urls import path
from . import views

#articles 경로 요청시 전체 게시글 목록을 확인할 수 있어야 함
app_name = 'articles'
urlpatterns = [ 
    #전체 게시글 목록을 확인할 수 있어야 함
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), #create 경로로 전송 -> 경로 위치 확인
    path('create/', views.create, name='create'),
]
