
from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.location),
    path('locations/<int:location_pk>/stations/', views.create_station),
    #전체 목록 조회
    path('stations/', views.station), #station 과 관련된 동작
    path('stations/<int:station_pk>/', views.station_detail), #station 과 관련된 동작

]
