from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

#수정은.. crate와 약간 유사한데 instance도 받고, partial을 설정해줘야 함        
@api_view(['GET', 'PUT', 'DELETE']) #삭제 -> 이건 serializer랑 상관없이 특정 내용 삭제 => 단 message를 내보낸다.
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk) #이걸 같이 사용 할 것이니까
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == "PUT": 
        serializer = ArtistSerializer(artist, data=request.POST, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) #수정 완료
    elif request.method == "DELETE":
        message = {
            "delete" : f"등록 번호{artist.pk}번의 {artist.name}을 삭제하였습니다."
        }
        artist.delete() #그냥 삭제하고 내보낸다
        return Response(message, status=status.HTTP_204_NO_CONTENT) #204코드반환
        #여기 보면 serializer.data 자리에 위 dict를 넘겨줘서 필요한 데이터를 넘겨줄 수 있다고 적혀있다.
        
