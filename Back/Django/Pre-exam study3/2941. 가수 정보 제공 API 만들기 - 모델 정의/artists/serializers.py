from .models import Artist
from rest_framework import serializers

class ArtistSerializers(serializers.ModelSerializer): #직렬화 생성
    class Meta:
        model = Artist
        fields = "__all__"