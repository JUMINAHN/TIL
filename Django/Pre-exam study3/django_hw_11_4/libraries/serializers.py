from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class ReviewListSerializer(serializers.ModelSerializer):
    #전체 조회에서
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ("isbn",)
    book = BookSerializer(read_only=True) #이것을 넣음
    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)



class BookSerializer(serializers.ModelSerializer):
    #여기서 모든 리뷰의 정보를 제공하도록 수정
    #review를 참조할 수 없으니 역참조 => 정보가 많고 읽기 전용
    #content와 score만 나오게
    review_set = ReviewListSerializer(many=True, read_only=True) #읽기 전용
    review_count = serializers.IntegerField(source="review_set.count", read_only=True)#count도
    class Meta:
        model = Book
        fields = '__all__'


    