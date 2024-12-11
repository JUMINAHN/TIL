from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Location, Station
from .serializers import LocationSerializer, StationListSerializer, StationSerializer

# Create your views here.
@api_view(['POST'])
def location_create(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def station_create(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE']) #여기서 location의 address값을 제공해야 한다
#현재 station의 address column은 참조 대상인 pk값을 제공해야 한다.
#여기임
def station_detail(request, station_pk):
    station = Station.objects.get(pk=station_pk) #매칭되는 친구가 존재하지 않는다..?
    if request.method == 'GET':
        serializer = StationSerializer(station)
        return Response(serializer.data)
    elif request.method == "DELETE":
        message = {
            "delete" : f"{station.address}의 등록 번호 {station.pk}번 충전소 정보를 삭제하였습니다."
        }
        station.delete()
        return Response(message, status=status.HTTP_204_NO_CONTENT)
        #str을 구현할수도 있데
