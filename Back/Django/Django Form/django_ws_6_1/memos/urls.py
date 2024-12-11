from django.urls import path
from . import views 

app_name="memos"
urlpatterns = [
    path('', views.index , name="index"), #index화면
    #게시글 생성하기 -> 생성에 응답과 요청이 발생한다. form을 활용해야 한다는 점 유의하기
    # path('new/', views.new, name="new"), #새로운 값을 생성하는 페이지 -> form을 사용할 것
    #생성을 받을 곳
    path('create/', views.create, name="create"),
    #index에서 더 상세적인 내용을 담는 것이니까 -> 순번 즉 pk를 기반으로 붙을 것임
    path('<int:pk>/', views.detail, name="detail"), #detail값을 받아올텐데,, 한개만 받아오는게 아니라 여러개 받아옴
    #게시물 삭제 기능을 만든다.
    path('<int:pk>/delete/', views.delete, name="delete"),
]
