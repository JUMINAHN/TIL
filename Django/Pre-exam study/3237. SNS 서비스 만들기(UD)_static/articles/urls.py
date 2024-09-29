from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    #삭제 기능 구현 == form 관련은 생성/수정관련
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    #수정 -> 수정 진행
    # path('<int:article_pk>/edit', views.edit, name="edit"),
    path('<int:article_pk>/update/', views.update, name="update"),
]