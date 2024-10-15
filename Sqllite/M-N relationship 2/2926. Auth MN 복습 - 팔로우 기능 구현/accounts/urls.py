from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<username>/', views.profile, name='profile'),
    #근데 왜 user는 pk로 안받고 name으로 받은 것인지 궁금함

    #follow 요청을 위한 url
    #follow는 user들의 정보를 기반으로 이루어짐 -> 따라서 계정 accounts/1/
    #이게 아니면 이름
    #path('<username>/follow/', views.follow, name="follow"),
    path('<str:username>/follow/', views.follow, name="follow"),
]
