from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')

def detail(request,pk): #상세 게시글 확인을 위한 데이터 
    #detail인것을 어떻게 확인하는가? == 기존과 동일
    article = Article.objects.get(pk=pk) #그거 받아서 -> 페이지에 보여줄 것
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
#상기와 동일 -> 대신 삭제했기 떄문에 데이터를 리다이랙트 해줘야 함
def delete(request, pk) :
    article = Article.objects.get(pk=pk) #삭제 요청 post로
    article.delete() #삭제 
    return redirect('articles:index') #메인으로 돌려주기 