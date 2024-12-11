from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
    #리뷰 생성 링크 => article에서 시작됨
    path('libraries/<int:book_pk>/reviews/', views.review_create),
    #리뷰 자체의 전체 조회 기능 구현 => get 
    path('reviews/', views.review_list), #comment_list
    #특정 reviews에 접근해야하니까 또 다른 url을 만들어야함을 명심!!
    path('reviews/<int:review_pk>/', views.review_detail),
]
