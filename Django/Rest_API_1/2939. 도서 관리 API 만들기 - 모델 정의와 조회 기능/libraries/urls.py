from django.urls import path
from . import views

#templates를 사용하지 않아도 됨
#json파일로 제공해야한다. ==serial izers -> 직렬
urlpatterns = [
    #직렬화를 진행할 수 있는 경로 제공 == 전체 조회
    path('', views.index), #name 필요없음 
    #detail 페이지 -> 요청항목을 보니 기존과 유사 구조
    path('<int:book_pk>/', views.detail) #pk는 어떠한 pk? -> book의 정보 한개 중
]
