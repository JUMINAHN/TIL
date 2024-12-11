from django.shortcuts import render
from rest_framework.response import Response
# from libraries.models import Book
from .models import Book
# from libraries.serializers import BookSerializer
from .serializers import BookListSerializer, BookSerializer
#여기서는 api_view를 받아줘야한다
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404 #객체가 존재하지 않을경우 자동으로 404 오류

@api_view(['GET'])
def index(request) : #request 
    book = Book.objects.all() #모든 정보 조회
    #북과 관련된 정보를 serilizer해야함
    serializer = BookListSerializer(book, many=True) #많은 정보들을 => context로 templates 보낸 것을 여기서는 json으로 전달한다.
    # print(serializer, '일반 serializer')
    # print(serializer.data)
    return Response(serializer.data) #serializer내부에 이것저것있는데 우리가 원하는 것은 data의 일부임
    #일단 데이터를 보낸 것을 확인해본다.
    #보면 title만 받고 싶어하는 것을 볼 수 있음

@api_view(['GET'])
def detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)  # 객체가 없으면 Http404 발생
    serializer = BookSerializer(book)
    return Response(serializer.data)

# #detail page
# @api_view(['GET']) #정보 확인이 목적 == 정보 조회
# def detail(request, book_pk):
#     book = Book.objects.get(pk=book_pk) #book -> pk
#     #같은 serializer을 사용하면 => 내가 원하는 4가지의 정보를 얻을 수 없음을 확인할 수 있음
#     serializer = BookSerializer(book) #book에 대한 정보 serializer #단순 조회
#     return Response(serializer.data)


# 단순 django view를 사용했을 때

from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()  # 모든 책 정보 조회
    context = {
        'books': books
    }
    return render(request, 'books/index.html', context)  # 템플릿에 데이터 전달

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # pk로 책 정보 조회
    context = {
        'book': book
    }
    return render(request, 'books/detail.html', context)  # 템플릿에 데이터 전달