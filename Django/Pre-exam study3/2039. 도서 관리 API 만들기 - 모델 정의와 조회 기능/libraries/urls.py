from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), #index view를 실행해야 함
    path('<int:book_pk>', views.detail, name="detail"),

]
