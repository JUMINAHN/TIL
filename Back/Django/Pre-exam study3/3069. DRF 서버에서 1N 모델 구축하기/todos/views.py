from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer, RecommendSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['DELETE', 'GET'])
def todo_detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #todo 정보 조회하기 => 상세정보 조회 :: 여기에서 recommend 내용 확인해야 함
    elif request.method == "GET":
        serializer = TodoSerializer(todo)#정보 조회 => many는 사용할필요가 없음
        #해당 정보 조회
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def recommend_create(request, todo_pk): #댓글 생성
    #post인 경우 데이터를 생성할 수 있도록
    todo = Todo.objects.get(pk=todo_pk)
    serializer = RecommendSerializer(data=request.data) #댓글의 data
    if serializer.is_valid(raise_exception=True):
        serializer.save(todo=todo) #todo값을 넣고
        return Response(serializer.data, status=status.HTTP_201_CREATED) #생성 완료

