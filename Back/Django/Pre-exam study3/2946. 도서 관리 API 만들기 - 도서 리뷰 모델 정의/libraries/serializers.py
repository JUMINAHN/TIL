from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

#review 전체 조회 기능 => content와 score정보만 제공
class ReviewPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("content", "score",) #book 외래키..
        #나머지는 자동 => 전체 나오는 것?

#review 생성
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__" 
        read_only_fields = ("book",) #model을 참고해서 외래키인 대상을 넣음