#외부 api정보를 model에 담기 위함 => 변환하기 위한 과정

from .models import Book
#serializer
from rest_framework import serializers

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", )

class BookSerializer(serializers.ModelSerializer): #따로 선언을 하는 이유는 => 다른 출력값을 얻기 위함
    class Meta:
        model = Book
        fields = "__all__"