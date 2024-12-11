
from .models import Todo
#serializer를 불러와야 함
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer): #model 따옴
    class Meta:
        model = Todo
        fields = "__all__"