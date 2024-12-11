
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name="create") #create 메서드 만들기 
]
