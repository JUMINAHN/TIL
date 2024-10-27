from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class ReviewListSerializer(serializers.ModelSerializer): #모든 리뷰의 정보가 나올 수 있도록 
    #전체 조회 페이지에서 리뷰가 참조하고 있는 도서의 isbn 정보를 제공하도록
    #리뷰가 참조하고 있는 도서
    #book이 가지고 있는 isbn을 조회하고 싶은 것
    #정참조?
    class BookSerializer(serializers.ModelSerializer): #detail에서 지금 사용하고 있음 => 여기서 모든 리뷰의 정보를 제공하도록 serializer를 수정
        class Meta:
            model = Book
            fields = ("isbn", ) #isbn에 대한 정보만 제공하고 싶다
    #book.isbn에 접근이 불가능..    
    book = BookSerializer() #book에대한 정보를 모두 가져오고 싶음 그런데 review_set, count는 뺴고
    #review자체가 instance를 가지고 있는데
    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

class BookSerializer(serializers.ModelSerializer): #detail에서 지금 사용하고 있음 => 여기서 모든 리뷰의 정보를 제공하도록 serializer를 수정
    # 즉 여기에서 모든 리뷰의 정보가 나올 수 있도록 해줘야 함
    #이 내부에서 선언하게 만들 것인데..  -> 어떠한 instance에? 
    #book이 직접적으로 참조하고 있는게 아니기 떄문에 역참조를 해야하지 않는가?
    #따라서 거기에 맞는 instance를 넣어서 값이 나오게 해야함 => 즉 전체리스트가 나오도록
    #이 친구 자체를 그대로 받았기 떄문에
    class ReviewListSerializer(serializers.ModelSerializer): #모든 리뷰의 정보가 나올 수 있도록 
        class Meta: #내부에서 오버라이딩!!
            model = Review
            fields = ('content', 'score',)
    review_set = ReviewListSerializer(many=True, read_only=True) #이친구가 들어갈 수 있도록 => book만 고려할 수 있도록 만들 수 있음
    #이름을 바꾸고 싶다면 => related_to에서 바꿔주면 된다.
    #역참조한 것들의 개수 -> 또 따로 국룰인 것 == 이것도 readonly
    review_count = serializers.IntegerField(source="review_set.count", read_only = True)
    #serializers.IntegerField는 시리얼라이저 필드 중 하나 => 정수값처리
    #시리얼 라이즈 한다
    #단일 게시글 댓글 목록
    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)

    