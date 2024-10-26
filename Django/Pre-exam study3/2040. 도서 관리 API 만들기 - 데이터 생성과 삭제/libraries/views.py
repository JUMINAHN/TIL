from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookListSerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404 

@api_view(['GET', 'POST']) #생성 => post메서드 추가
#이제 get과 포스트를 사용 
#기본 세팅값은 get인것을 알 수 있음
def index(request) :
    if request.method == 'GET':
        books = Book.objects.all() #해당 키워드로 사용할 것이니까 
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data) 
    elif request.method == "POST": 
        #기존 book에 맞게 -> 데이터를 받아와야 함 : 생성된 것
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :#예외처리
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'DELETE'])
def detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk) #같이 사용할거니까 if 밖으로 일단 뺏고
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == "DELETE": #delete일 때
        #message 삭제 -> 디테일한 것을 삭제해야함 => 기존 article을 제거했을 떄를 떠올려보면
        #특정 메서드 조회되면.. => 따라서 그 메서드의 유무 확인
        book.delete() #삭제하고-> 삭제했다고 나타냄 : 그냥 book자체를 삭제하는 것 
        #역직렬화로 보내주는 것보다 그냥 삭제 -> statuss
        #f-string없이
        serializer = BookSerializer(book)
        #return Response(serializer.data)
        #예외처리에서 나타나는 not found를 수정한 것인지? -> delte시에만 작동되어야 하는데..
        return Response(f'"delete" : 도서 고유번호{book.isbn}번의 {book.title}을 삭제하였습니다.') #상태코드이야기 보다는 반환값을 주긴 함
""

#단순 조회 ->
#aritcle.delete() => 그리고 그냥 페이지 리턴 : 아마 동일한 구조로 진행될 것 