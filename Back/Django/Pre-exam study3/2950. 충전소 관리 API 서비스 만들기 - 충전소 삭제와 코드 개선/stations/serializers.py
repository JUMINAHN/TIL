from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    #여기서 참조해야한다 => 무엇을?  location의 address값을
    class LocationSerializer(serializers.ModelSerializer):

        class Meta:
            model = Location
            fields = ("address", )
    address = LocationSerializer(read_only=True) #여기에 location address값, 읽기 전용
    #이걸 제공할 수 있도록 수정
    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address', )

class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        

        