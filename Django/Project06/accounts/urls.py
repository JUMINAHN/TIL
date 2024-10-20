from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #path profiles => 근데 프로필 페이지는 여러 유저가 올 수 있음
    #바로 user의 정보를 담게 되면, risk가 발생함 => 따라서 어떠한 기능에 유저가 오는지를 명시해두는게 좋음
    path('profiles/<str:username>/', views.profiles, name="profiles"), #아마 userpk를 작성해도 무방할 것이나 -> 사용자 친화성을 위해 username
    #user의 follow기능 구현 => 해당 부분 profiles에서 진행되는 것 => url을 딱히쓸필요가 없나? => view를 사용해야 하는데
    #해당 유저를 follow => 해당 유저를 팔로우하는 것
    path('<int:user_pk>/follows/', views.follows, name="follows"), #follow하는 것
]
