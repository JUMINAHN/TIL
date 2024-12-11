from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class ReviewListSerializer(serializers.ModelSerializer): 
    class BookIsbnSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ("isbn", ) #isbn

    # #book에 대한 isbn 정보? -> review
    #Review가 Book을 참조하는 방식으로 book 필드를 사용
    # Review에서 book 필드(인스턴스 보유) 를 통해 직접적으로 Book 모델의 정보를 가져올 수 있다.
    book = BookIsbnSerializer(read_only=True) #조회 시에만 사용하도록 -> read_only사용
    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)


class BookSerializer(serializers.ModelSerializer): #상세 정보 페이지에서 도서를 참조하고 있는 모든 리뷰의 정보를 제공할 수 있도록
    class ReviewListSerializer(serializers.ModelSerializer): 
        class Meta:
                model = Review
                fields = ('content', 'score',)

    class Meta:
        model = Book
        fields = '__all__'
    review_set = ReviewListSerializer(many=True, read_only=True) #관계된 객체를 읽기 전용으로 직렬화
    review_count = serializers.IntegerField(source="review_set.count", read_only=True) #이미 계산된 값이므로 사용자가 직접 설정할 수 없음
    #이는 정수 값을 나타내는 직렬화 필드
    #integerfield와 유사

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)