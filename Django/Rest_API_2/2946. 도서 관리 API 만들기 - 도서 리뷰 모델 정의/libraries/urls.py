from django.urls import path
from . import views


urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
    #리뷰 생성 -> 특정 게시글 아래에 여러 댓글들이 달림 
    #댓글들을 지정하는게 아니니 특정 게시글 아래에 코멘트
    path('libraries/<int:book_pk>/review_create/', views.review_create),
    #리뷰 전체 조회
    path('reviews/', views.book_review) #단순 조회 -> reviews
]
