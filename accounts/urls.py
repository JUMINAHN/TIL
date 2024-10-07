from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [ #유저목록을 전체 확인할 수 있는 페이지를 구현 -> accounts내부에서 생성
    #url -> views를 호출해야 함
    path('', views.index , name="index"),
    #loginpage 구현 -> loginpage를 구현하기 위해선 loginform을 사용하는 페이지와 그걸 다룰 수 있는 곳이 필요
    #이전의 new와 create와 같은 구조임
    path('login/', views.login, name="login"),
]
