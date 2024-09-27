from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.index, name="index"),
    #생성하기
    # path("new/", views.new, name="new"),
    path("create/", views.create, name="create"), #생성에서 지금 문제가 됨 -> this field is required 보냈는데
    path("<int:pk>/", views.detail, name="detail"),
    #삭제 버튼 -
    path("<int:pk>/delete/", views.delete, name="delete"),
    #수정 페이지
    # path("<int:pk>/edit/", views.edit, name="edit"), #edti -> updates
    path('<int:pk>/update/', views.update, name="update"),
]
