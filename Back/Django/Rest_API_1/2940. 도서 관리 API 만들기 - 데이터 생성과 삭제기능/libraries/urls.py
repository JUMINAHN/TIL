from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
    #단순 생성 진행
# /    path('libraries/create/', views.book_create),
]
