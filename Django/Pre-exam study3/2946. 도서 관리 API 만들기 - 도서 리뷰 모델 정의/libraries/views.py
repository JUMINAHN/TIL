from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Book, Review
from .serializers import BookListSerializer, BookSerializer, ReviewPartSerializer, ReviewListSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': #단순 정보
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


#review 전체 출력
@api_view(['GET'])
def review_list(request):
    #리뷰 전체 조회 기능 => 기존과 상동
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewPartSerializer(reviews, many=True)
        return Response(serializer.data) #review와 관련된 내용 모두 전체 조회
        #content와 score의 기능만 제공한다
    

#그러면 여기서 추가로 삭제, 수정에 대해서 연습해보자
@api_view(['POST', "DELETE", "PUT"])
def review_create(request, book_pk):
    #일단 생성 -> 한개만 있으니까
    if request.method == "POST":
        book = Book.objects.get(pk=book_pk)
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book) #기존 post와 일단 동일하게 만들어보자
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#comments는 또 따로
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk) #특정 review
    if request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT": #기존 게시글 수정과 비슷함 
        #serializer에 데이터가 없다는 의미인가?
        serializer = ReviewPartSerializer(review, data=request.data, partial=True) #교재에서는 여기에 True가 아님 -> partial이 일부분 변환?
        if serializer.is_valid(raise_exception=True) : 
            serializer.save() #db에 저장 => 특정값에 저장
            return Response(serializer.data, status=status.HTTP_200_OK) #status도 안보냄
    elif request.method == "GET":
        serializer = ReviewPartSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)