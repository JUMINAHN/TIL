from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistPartSerializer


# Create your views here.
@api_view(['GET','POST'])
def artist_list_or_create(request):
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True): #필요한것만 만들고
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET': #모든 정보 제공
        artists = Artist.objects.all() #모든 artists
        serializer = ArtistPartSerializer(artists, many=True) #많은 정보들 조회
        return Response(serializer.data)
    
#상세정보에는 모든 것을 출려갛고 싶음
@api_view(['GET']) #어짜피 이것도전체 조회
def detail_or_sth(request, artists_pk):
    artist = Artist.objects.get(pk=artists_pk) #모든 artists
    serializer = ArtistSerializer(artist) #많은 정보들 조회
    return Response(serializer.data) #모든 정보
