from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"), #전체 유저 목록을 확인할 수 있는 페이지 구성
    #login page 구현 == login은 요청/응답을 하는 곳 -> form 조회 응답
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout") #이건 요청과 응답이 이루어지지만 -> page필요없음
]
