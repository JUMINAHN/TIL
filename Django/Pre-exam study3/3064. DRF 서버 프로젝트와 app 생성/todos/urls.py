
from django.urls import path
from . import views

urlpatterns = [ #경로는 api임을 알 수 있도록 api/v1으로 설정한다.
    path('', views.index, name="index"),
]
