from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), #해당 페이지에서 -> 조회, 생성 가능
    path('<int:book_pk>', views.detail, name="detail"),

]
