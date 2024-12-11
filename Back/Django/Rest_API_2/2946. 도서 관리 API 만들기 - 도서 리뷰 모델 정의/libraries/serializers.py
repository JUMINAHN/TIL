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


#리뷰 생성 기능 구현
#model form처럼 -> review라는 모델을 기반으로 만들어지는 것?
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__" #all이라서 여기에 작성된 필드는 모두 유효성 검사가 일어남 => 외래키의 여부
        read_only_fields = ("book",) #외래키가 있는 모델 -> 그 인스턴스를 지칭하는 필드 == book 이 부분을 읽기전용으로 해줘야 함
        #결과 데이터엔 포함하고 싶으나, 유효성 검사는 제외하게 된다. 
        #즉 == 클라이언트가 직접 수정할 수 없지만, 서버 측에서 값을 지정

#이제 리뷰의 전체 기능 제공 -> 단 리뷰의 content와 score의 정보만 제공한다.
class ReviewSerializer(serializers.ModelSerializer): #단순 리뷰 조회 
    class Meta:
        model = Review
        fields = ("content", "score", )
