from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
# 조회 => 무언갈 만들기
#status 호출
from rest_framework import status
from .serializers import ArtistSerializers
from .models import Artist #생성에는 사용하지 않음

#생성하기
@api_view(['POST'])
def create(request):
    #페이지 생성은 내부적으로 만들어 줌
    serializer = ArtistSerializers(data=request.data) #requestdata가
    #이것에 대한 유효성 검증을 실시해야 함
    if serializer.is_valid(raise_exception=True): #예외 발생시 400코드를 발생할 수 있도록
        serializer.save() #저장을하고
        return Response(serializer.data, status=status.HTTP_201_CREATED) #data를 돌려주고, 성공 버튼 줘야함
        #데이터 보여줄거니까
    #return Response(se)
