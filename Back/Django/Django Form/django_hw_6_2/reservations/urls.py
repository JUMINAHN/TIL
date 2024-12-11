from django.urls import path
from . import views


app_name = 'reservations'

urlpatterns = [
    path('', views.index, name='index'),
    #form을 작성한다는 의미는 new와 create를 한다는 것
    #new로 경로 요청이 들어오면 new view함수를 실행한다.
    path('new/', views.new, name='new'),
    #생성을 한다.
    path('create/', views.create, name='create'),

]