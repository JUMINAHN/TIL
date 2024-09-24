from django.urls import path
from . import views

app_name = 'garages'
urlpatterns = [
    path('', views.index, name='index'), #모든 정보를 확인할 수 있어야 한다.
    #new 경로로 접근시 form으로 정보를 입력받는다
    #즉 new와 create
    path('new/', views.new, name='new'),
    #new를 받을 create 생성
    path('create/', views.create, name='create'),
]
