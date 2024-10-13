
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    #회원가입기능 구현 => login과 유사함
    path('signup/', views.signup, name="signup"),
]
