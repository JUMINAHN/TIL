from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    #리뷰 등록 url 작성
    path('<int:book_pk>/review/create/', views.review_create, name="review_create"),
    #delete버튼은 review까지는 동일하되, book이 아니라 user에 대한 정보를 받아와야 함
    #review_pk? user_pk?
    path('<int:book_pk>/review/<int:review_pk>/delete', views.review_delete, name="review_delete")
]
