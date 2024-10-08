from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"), #index
    path('login/', views.my_login, name="my_login"),
    #회원가입 폼 잠석
    path('signup/', views.signup, name="signup"),
]
