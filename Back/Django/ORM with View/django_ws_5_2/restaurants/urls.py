from django.urls import path
from . import views


app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), #새로운 것 만들기
    path('create/', views.create, name='create'), #실제 생성을 위한 view
    path('<int:pk>/', views.detail, name='detail'), #상세 정보를 알려준다.
    #삭제를 하자
    path('<int:pk>/delete', views.delete, name='delete'), #delete키로 삭제
    path('<int:pk>/edit', views.edit, name='edit'), #edit
    path('<int:pk>/update', views.update, name='update')

]