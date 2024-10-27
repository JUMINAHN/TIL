from rest_framework import serializers
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name', 'debut_date',)

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'

#수정 가능 정보는 바뀌기 때문에 새로운 serializer를 설정 해야 함
class ArtistEditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ("agency", "is_group",)