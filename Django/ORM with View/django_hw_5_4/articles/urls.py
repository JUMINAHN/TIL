from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), #여러개중받은 것 -> create뒤에 붙는것이니까
    #그리고 이와 관련된 삭제 -> 해당 대상 요소를 삭제해야함 조회하고
    path('<int:pk>/delete/', views.delete, name='delete')

]

