from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def fetch_todo(request, todo_pk):
    if request.method == 'GET':
        todos = Todo.objects.get(id=todo_pk) #id값이 pk인 것
        serializer = TodoSerializer(todos)
        return Response(serializer.data)