"""
URL configuration for todo_list_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', views.index), #여기 수정, variable routing을 활용하기 위해서 
    path('todos/create_todo/', views.create_todo), #위치탓..? #이거 왜 위치 타나요?
    path('todos/<str:work>/', views.detail), #여기 수정, variable routing을 활용하기 위해서 
]
