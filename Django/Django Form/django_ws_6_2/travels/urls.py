from django.urls import path
from . import views

app_name = "travels"
urlpatterns = [
    path('', views.index, name="index"),
    #게시글 생성 페이지 -> new와 create
    #new에서 form을 받고 create로 요청을 받아서 전체에 뿌려주는 것
    # path('new/', views.new, name="new"), #form을 사용하려면 form 태그가 있어야 한다.
    path('create/', views.create, name="create"),
    #상세 페이지 생성
    path('<int:pk>/', views.detail, name="detail"),
]
