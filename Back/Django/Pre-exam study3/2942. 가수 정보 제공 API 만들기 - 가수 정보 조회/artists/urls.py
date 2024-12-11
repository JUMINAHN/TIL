from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_list_or_create), #name까지 만들 필요 없으니까
    path('artists/<int:artists_pk>/', views.detail_or_sth),
]
