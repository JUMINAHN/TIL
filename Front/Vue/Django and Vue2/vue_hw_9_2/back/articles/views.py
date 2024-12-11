from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# session이 걸려있어서 오류가 발생했었음 => 허가된 사용자는 생성가능!
@permission_classes([IsAuthenticated]) #허가된 인증된 사용자만 사용가능
def article_list_create(request):
    print('tt')
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
