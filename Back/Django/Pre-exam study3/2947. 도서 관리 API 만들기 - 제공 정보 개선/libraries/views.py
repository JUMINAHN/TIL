from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Book, Review
from .serializers import BookListSerializer, BookSerializer, ReviewListSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
#여기서 모든 리뷰의 정보를 제공하도록 수정하는 것 -> 이 자체에서는 변경하지 않음 : content와 score정보만 제공한다
#역참조 중인 리뷰의 총 수를 제공한다. 
#그냥 일반적인 경우? => 일단 조회를 했을 떄 
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk) #book과 매칭되는 쿼리가 없다
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        book.delete()
        data = {
            'delete': f'도서 고유 번호 {book.isbn}번의 {book.title}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all() #모든 리뷰가 나올 수 있도록 => list
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def review_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)