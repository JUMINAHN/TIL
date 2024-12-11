from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list),
    #수정
    path('todos/<int:todo_pk>/', views.fetch_todo),
]
