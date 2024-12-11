#serializers 
#rest_api
from rest_framework import serializers #직렬화하는 모듈
from .models import Book

#직렬화라는 키워드를 기반으로 -> 검색 진행 중
#직렬화!
#전체는 list로 받고, 일부는 그냥 단순 요소로 받자
class BookListSerializers(serializers.ModelSerializer): #serializers.ModelSerializer
    #? 다시 저장을 하니까 작동이 된다.
    class Meta:
        model = Book #BOOK 모델 사용
        fields = ('title', )#"__all__" #모든 필드 포함

#상세정보를 위한 serializer 생성 -> 사실 상기 코드를 사용해도 무관함
#그러나 여기서는 전체 정보를 요청하고 있음
class BookSerializers(serializers.ModelSerializer): #모델 사용
    class Meta:
        model = Book
        fields = "__all__"