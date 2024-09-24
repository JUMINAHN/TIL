from django.urls import path
from . import views


app_name = 'garages'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    #edit 경로에서 form을 제공한다.
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    #삭제를 해야 함
    path('<int:pk>/delete/', views.delete, name='delete'),
]
