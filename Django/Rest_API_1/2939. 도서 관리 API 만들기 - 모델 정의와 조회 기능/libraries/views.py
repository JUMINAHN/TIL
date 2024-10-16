from django.shortcuts import render
from .models import Book
#serializer은 소환해야함
from .serializers import BookListSerializers, BookSerializers #list
#response 호출
from rest_framework.response import Response
from rest_framework.decorators import api_view #decorator

#여러개 조회
# Create your views here.
@api_view(['GET']) #여러 메서드를 받을 수 있음 -> 일단 단순 조회
def index(request): #기존 request는 동일
    #전체 조회
    books = Book.objects.all() #book의 전체 정보
    #html에 전달하는게 아니라 api로 다룰 것
    #serializers(queryset, many)
    serializers = BookListSerializers(books, many=True) #book의 데이터를 다룰 것 == 여러개 조회
    return Response(serializers.data) #돌려주는 것은 작성
    #객체 단위가 아니라 -> dictionary로 사람들이 읽을 수 있도록 생성

@api_view(['GET'])
def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk) #특정 정보
    serializer = BookSerializers(book) #모든 정보 추출 -> 정보 많이 받을필욘X
    #동일하게 돌려줄 것
    return Response(serializer.data)