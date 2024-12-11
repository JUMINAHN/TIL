from django.urls import path
from . import views #todos자체를 호출할필요가 없음
# 자기자신 .을 호출
app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'), #todos/자체가 애초에 연결 링크였기 떄문에
    #views는 수정할 부분이 없음
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<work>/', views.detail, name='detail'),
]

