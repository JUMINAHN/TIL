from django.urls import path
from . import views 
# 자기자신 .을 호출
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'), #접속은 맞게 들어와지는데 템플릿이 없다고 뜸
]