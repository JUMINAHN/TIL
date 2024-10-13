from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):  #전체 내용을 담을 것이기 때문에
    articles = Article.objects.all() #모든 정보 가져오기 -> 사용할 것이니까 main 전달
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request): #new -> request
    #새로운 페이지 전달 -> 이건 form tag 사용했었음!
    #지금은 그냥 페이지 링크만 전달하면 됨
    return render(request, 'articles/new.html') #추후 name에서 detail활용

def create(request): #상기와 동일하게 form으로 data랑 files, post 모두 받았고
    #그리고 그것에 대한 유효성 검사를 진행하고 -> data를 보내야했었음
    #남은 data에 대한 context도 전달하고 그랬었음 => 특정폼(request.POST, request.FILES)
    #일단 이것은 요청받은 form 데이터를 db에 넣기 위한 작업 중 하나
    #아마 각 데이터에 대한 정보를 요청에 따라 받아와야 함
    title = request.POST.get("title") #articles에 대한 정보를 받아오는데 -> 이것은 어디 name?
    content = request.POST.get("content")
    #article = Article() #article을 생성하고 기존에 했던 것을 진행 -> 2번째 방식많이 사용
    #article = Article("title":title, "content":content) => text라고 잘못 기입함
    # article = Article(title=title, content=content)
    article = Article()
    article.title = title
    article.content = content
    article.save() #유효성 검사 추후 진행 -> 그리고 받은 내용의 데이터를 돌려주나? ㄴㄴ
    #저장한 정보를 메인으로 돌려줘야함
    return redirect('articles:index')