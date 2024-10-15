from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    #pofile => account 페이지에서 접근이 가능함
    #profile/sthing의 구조로 받을 것
    #단순 <> : 구조로 받을 경우 모든 string 관련 파일이 저쪽으로 들어가게 되는 오류를 범함
    #그리고 갑자기 궁금한거 str:user_pk, user_pk:str차이?
    path('profiles/<str:username>/', views.profile, name="profile"),
    
]
