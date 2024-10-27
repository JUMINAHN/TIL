from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data) #post요청이니까
        #유효성 검사 시작
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['DELETE'])
def todo_detail(request, todo_pk): #특정 내용 삭제
    #todo
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT": #수정 => 이것 없어도 되는데?
        serializer = TodoListSerializer(todo, data=request.data, partial=True) #post요청이니까
        #유효성 검사 시작
        if serializer.is_valid(raise_exception=True): #수정하게 한다
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)