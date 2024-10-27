from rest_framework import serializers
from .models import Todo, Recommend



class RecommendSerializer(serializers.ModelSerializer): #데이터를 생성할 수 있도록 => 모두 출력
    class Meta:
        model = Recommend
        fields = "__all__" #모두
        read_only_fields = ("todo",)

class TodoSerializer(serializers.ModelSerializer): #정보가 부족한 것 같음
    #여기서 밑에 recommend정보를 얻어야 함
    #recommendSerializer 얻으면 됨
    #todo 자체에서ㄴ까 역참조해야함
    class RecommendSerializerForTodoDetail(serializers.ModelSerializer): #데이터를 생성할 수 있도록 => 모두 출력
        class Meta:
            model = Recommend
            fields = ("id", "content",)#모두
            read_only_fields = ("todo",) #여기 todo 없어야함
            #todo는 exclude를 사용해서 제외시킨다? => 이거 사용하지 않고 일단 한다
    recommend_set = RecommendSerializerForTodoDetail(many=True, read_only=True) #호출하고 결과 데이터

    #request.data를 기반으로 recmommend를 생성할 떄, 참조할 대상 todo 정보 삽입
    class Meta:
        model = Todo
        fields = '__all__'

    
class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )

