"""
URL configuration for my_fifth_project project.

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

#articles 경로 요청시 전체 게시글 목록을 확인할 수 있어야 함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), #없데 왜 맞게했자너
    #또 여기서 오류 include는 .으로 진행해줘야 함 ㅠㅠ 계속 실수
    #혹시 못찾게 되면 여기서 문제가 발생한 것으로 인지할 것
]
