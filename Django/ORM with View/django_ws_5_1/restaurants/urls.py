from django.urls import path
from . import views

app_name = 'restaurants' #restaurants는 등록 되지 않은 이름이다.
urlpatterns = [
    path('', views.index, name='index'),
    #새로운 식당 생성을 위한 form을 위한 new
    path('new/', views.new, name='new'),
    #그리고 그 요청을 받을 create
    path('create/', views.create, name='create'),
]
