"""
URL configuration for my_pjt project.

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
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #username으로 경로로 요청을 보내면, introduce view함수가 실행되어야 한다.
    #URL기반으로 요청을 보냈을때, 계속해서 값이 달라질 수 있음 따라서
    #<str:name>이런 형식으로 접근해야 함
    path('introduce/<str:name>/', views.introduce)
]
