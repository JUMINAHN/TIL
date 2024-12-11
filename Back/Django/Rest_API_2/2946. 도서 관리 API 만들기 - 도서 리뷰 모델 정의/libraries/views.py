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
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        book.delete()
        data = {
            'delete': f'도서 고유 번호 {book.isbn}번의 {book.title}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST']) #리뷰 생성
def review_create(request, book_pk): #특정 게시글에 리뷰를 작성해야 함 -> 특정 게시글 참조
    book = Book.objects.get(pk=book_pk) #특정게시글
    serializer = ReviewListSerializer(data=request.data) #받아서 생성 == 사실상 리뷰와 관련된 네용
    if serializer.is_valid(raise_exception=True): #exception == True #그리고 외래키를 -> 있는지 확인을 이곳에서 함
        serializer.save(book=book) #리뷰 생성
        #즉 특정 책과 리뷰를 연결하는 것
        #review model에 있는 book인스턴스에 특정 게시글이 무엇인지에 대한 것을 대입
        #즉 외래키 데이터 입력 후 저장
        #설계도상 참조값을 넣는 곳? Q?
        return Response(serializer.data, status=status.HTTP_201_CREATED) #아니면 404반환,, -> raise_Exception
    
@api_view(['GET'])
def book_review(request): #리뷰 조회
    #리뷰 -> 게시글이 아닌 리뷰
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data) #해당 데이터 전달