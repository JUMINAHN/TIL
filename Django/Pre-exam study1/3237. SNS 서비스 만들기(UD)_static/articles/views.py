from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

#detail 페이지에서 이루어짐 -> form자체에 요청을 받아서 진행되는 것
def delete(request, article_pk): #삭제할 것 -> form자체에 데이터를 받아오는데..
    article = Article.objects.get(pk=article_pk)
    article.delete() #기존에는 이렇게 작성함 -> 받아온 것..? 이렇게 활용하는 것 아닌가
    return redirect('articles:index') #index page로 다시 돌려주기

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article) #파일도 업데이트 해야함
        if form.is_valid(): #유효성 검사
            form.save() #mainpage로
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article) #그냥 해당 정보를 받아옴 -> 기존 정보에 대한 article을
    #그것에 대한 편집 진행 -> 편집 링크를 보내줌
    context = {
        'form' : form,
        'article' : article #aritlce에 대한 정보도 리턴
    } #편집 사이트로 -> form으로 기존 정보 활용해야 하니까
    return render(request, 'articles/update.html', context)


#new와 동일
#세부정보를 일단 받아와야함 -> new에서는 받아올 필요가 없었음
#원래 기존에는
#request.POST.get("name안에 속성") = 받아서
#기존 -> 수정진행했었음
# #이것도 기존내용과 동일한 것 같음
# def edit(request, article_pk):
#     #form으로 기존 내용들 다시 다 받아오기
#     article = Article.objects.get(pk=article_pk) #상세 세부 내용
#     form = ArticleForm(instance=article) #그냥 해당 정보를 받아옴 -> 기존 정보에 대한 article을
#     #그것에 대한 편집 진행 -> 편집 링크를 보내줌
#     context = {
#         'form' : form
#     } #편집 사이트로 -> form으로 기존 정보 활용해야 하니까
#     return render(request, 'articles/edit.html', context)

# def update(request, article_pk):
#     #수정된 내용 반영 -> 기존 데이터에 반영
#     article = Article.objects.get(pk=article_pk)
#     form = ArticleForm(instance=article)
#     if form.is_valid(): #유효성 검사
#         form.save() #mainpage로
#         return redirect('articles:index')
#     context = { #그게 아니면 다시 내용 수정
#         'form' : form, #form내용과 article에 대한 정보 받아가기 다시
#         'article' : article #딱히 필요없어 보이긴 함
#     }
#     return render(request, 'articles/edit.html', context)

