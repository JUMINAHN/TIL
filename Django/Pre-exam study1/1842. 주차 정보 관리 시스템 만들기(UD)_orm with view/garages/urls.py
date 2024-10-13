from django.urls import path
from . import views


app_name = 'garages'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    #상세정보 페이지 생성 후 -> edit 페이지 생성
    path('<int:pk>/', views.detail, name="detail"),
    #삭제하기
    path('<int:pk>/delete/', views.delete, name="delete"),
    #수정 업데이트 하기 -> 수정 form 만들기
    path('<int:pk>/edit/', views.edit, name="edit"), #name 잘 활용하기
    #수정 업데이트한 고객의 요청을 db에 담고 응답을 돌려줄 페이지
    path('<int:pk>/update/', views.update, name="update"),
]
