from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context) #여기서 에러가 터지는데 ?? why

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')

def detail(request, pk): #detail한 내용 -> 매개변수 인자 있는데 ? 
    #pk로 전달받아서 해당 내용 활용할 것
    articles = Article.objects.get(pk=pk) #pk를 인자로받아서 확인하고
    #이걸 content에 보낼 것
    context = {
        'articles' : articles
    } #상세 페이지 자체를 보내준다. 보여준다.
    return render(request, 'articles/detail.html', context)

def delete(request, pk): #특정 요소를 삭제해야 함
    #조회하고 그냥 내용 받아서 삭제하면 됨
    #그러면 지금 Article에 있는 내용 조회하고 삭제하면 됨
    article = Article.objects.get(pk=pk)
    article.delete() #삭제
    #csf토큰
    return redirect('articles:index') #돌려줘야하나?
    #POST기 때문에 redirect로 메인 페이지로 돌려줘야 함

