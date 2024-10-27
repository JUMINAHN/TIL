from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:todo_pk>/', views.todo_detail),
    #todo 정보 조회하기
    path('todos/<int:todo_pk>/recommends/', views.recommend_create), #댓글 목록과 같은 기능을 할 것
]
