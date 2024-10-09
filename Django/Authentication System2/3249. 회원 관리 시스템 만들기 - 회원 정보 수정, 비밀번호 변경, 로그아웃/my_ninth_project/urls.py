"""
URL configuration for my_ninth_project project.

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
from django.urls import path, include
from accounts import views #account에 있는 view 사용


#passwordchangeform -> 자체 form 사용
#사용자 관련 ==> user 관련 등록 절차, 생성 etc 부분 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    #project 자체에 change_password를 해주어야 함 -> why? 
    #그리고 왜 int:pk를 해야하는 지?
    #user에 대한 정보 자체를 받아와야 함 
    path('<int:user_pk>/change_password/', views.change_password, name="change_password")
]

