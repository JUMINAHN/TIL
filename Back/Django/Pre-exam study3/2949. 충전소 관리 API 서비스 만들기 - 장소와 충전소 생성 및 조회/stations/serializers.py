from .models import Location,Station,Car
from rest_framework import serializers

#serializer => location
#전체를 보여줄 것
class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__" #모두 다 => 정보를 생성할 것 

class StationCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__" #입력값을 확인했을 때 === post
        #생성할때 location 정보는 직접 입력하지 않는다.
        #읽기 전용 모드를 설정해줘야 함
        #두개만 띄웠는데 opening을?
        read_only_fields = ("address", "is_opening") #사용자가 직접 입력하지 않아도 되는 필드들을 모두 포함시킨다

class StationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ("address", "is_opening", ) #전체 목록을 조회하는 것
        

class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__" #상세 목록을 조회하는 것 => 모든 정보를 제공한다