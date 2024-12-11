from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name="index"), #index -> view 실행
    #생성 기능 구현
    # path('new/', views.new, name="new"),
    #path('create/')
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
]
