from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    #좋아요 요청을 받을 수 있는 경로를 작성한다.
    #아티클과 M:N관계를 형성할 것이고 -> article을 기반으로 데이터를 받아올 것
    path('<int:pk>/likes/',views.likes, name="likes")
]
