from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer): #이건 전체 데이터를 보여주는 것
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "debut_date",)