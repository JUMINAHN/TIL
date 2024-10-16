from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer
#status -> 상태확인을 위해 status도 필요
from rest_framework import status
# Create your views here.
# Django의 Rest FrameWork의 가장 큰 장점 : 하나의 URL에서 여러 HTTP메서드 처리 가능
# 코드 중복을 줄이고, 유지보수 쉽게 함
# 삭제 기능

@api_view(['GET', 'POST'])
def book_list(request): 
    if request.method == "GET":
        books = Book.objects.all()
        #get을 통해서 전체 게시글을 가져옴 == 모든 데이터를 볼 수 있도록
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
        #post == 새로운 데이터 서버 추가 : 사용자가 보낸 유효성 검사하고, 올바르면 db에 지정
        #Q. 즉 api를 제공하는 서버에서 받은 데이터의 유효성 확인??
    elif request.method == "POST":  #전체 만들기
        #data를 받아서 넣기
        serializer = BookSerializer(data=request.data, many=True) #데이터 확인
        #유효성 검사 진행
        if serializer.is_valid():
            serializer.save() #유효성 검증 진행
            return Response(serializer.data, status=status.HTTP_201_CREATED) #201 status 코드 반환
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET' , 'DELETE']) #특정 데이터 삭제 #"DELETE /api/v1/libraries/1/ HTTP/1.1" 405 43 -> 누락시
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
        #삭제는 뭐 다른것을 할게 없다
    elif request.method == "DELETE":# 이전까지 게시글 삭제와 동일
        book.delete() #기존과 동일
        return Response(f'도서 고유번호 {book.isbn}번의 {book.title}을 삭제하였습니다' )


#기존에는 전체 게시글 조회, 단일 게시글 조회
#create관련
#생성 -> POST
#form 생성 -> form을 만들고 폼에 대한 정보를 주고 그것에 대한 정보를 받았음
#게시글 데이터 생성하기 
# def book_create(request): #book 생성 -> POST로 주는데 무엇을 조회함?
    


