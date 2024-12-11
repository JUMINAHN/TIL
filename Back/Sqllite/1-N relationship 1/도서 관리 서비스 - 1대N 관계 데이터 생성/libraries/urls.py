
from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name="index"), #view -> 접근
    #상세 정보에 접근해야 합니다.
    path('<int:author_pk>', views.detail, name="detail"), #url 링크가 author_pk인 것
    #저자가 책을 만들 것이니 -> 책을 생성하는 url을 만든다.
    #단, detail에 / books / 라는 것을 추가해서 book에 대한 세부 내용을 담는다
    path('<int:author_pk>/books/create', views.books_create, name="books_create"), #댓글 생성과 비슷한 개념
    #댓글 생성을 하려면 -> form이 필요함
]
