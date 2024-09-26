from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name="index"), #초기 경로 설정 -> 일단 이부분 확인을 위해 가동
    #생성기능을 구현해야 한다 -> new와 create를 생각하면 된다.
    # path('new/', views.new, name='new'), #지울 요소
    #create
    path('create/', views.create, name='create'), #생성할 것
    #이제 상세 페이지
    path('<int:pk>/', views.detail, name='detail'),
]