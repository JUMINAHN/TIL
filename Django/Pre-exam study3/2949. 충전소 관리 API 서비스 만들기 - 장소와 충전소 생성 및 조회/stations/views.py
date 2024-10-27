from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LocationSerializers, StationSerializers, StationListSerializers, StationCreateSerializers
from .models import Location, Station

# Create your views here.
@api_view(['POST'])
def location(request):
    #정보를 생성하는 것
    serializer = LocationSerializers(data=request.data) #이것을 적고 => 유효성 검사
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) #생성 성공

@api_view(['POST'])
def create_station(request, location_pk): #location 정보는 사용자가 직접 입력하지 않는다
    location = Location.objects.get(pk=location_pk) #이것 활용할 것
    serializer = StationCreateSerializers(data=request.data) #data자체를 받을 것이고
    #유효성 검사 진행
    if serializer.is_valid(raise_exception=True):
        serializer.save(address=location) #혹은 이자체에 명시적으로 설정 is_opening=False
        return Response(serializer.data, status=status.HTTP_201_CREATED) #성공적으로 만들어짐 => location 정보는사용자가 입력하지 않음 

#station 전체 목록 조회
@api_view(['GET'])
def station(request): #전체 목록 조회
    stations = Station.objects.all() #모든 목록
    serializers = StationListSerializers(stations, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK) #조회

#상세 정보 조회
@api_view(['GET']) #이것도 get
def station_detail(request, station_pk):
    stations = Station.objects.get(pk=station_pk) #하나
    serializers = StationSerializers(stations)
    return Response(serializers.data, status=status.HTTP_200_OK) #조회


