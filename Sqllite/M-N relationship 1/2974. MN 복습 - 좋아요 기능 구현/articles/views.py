from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

#조회 페이지 -> get을 사용할 이유가 없음 
#단, 로그인되어있는 유저만 좋아요 기능을 사용할 수 있음
@login_required
def likes(request, pk) : 
    article = Article.objects.get(pk=pk) #pk정보를 받고 이것을 활용
    #게시글 세부 정보를 받아올 수 있어야 함
    if request.user != article.user: #like의 요청이 들어왔을 때 게시글의 작성자 인지 아닌지
       #게시글의 작성자가 아닌 경우에만 좋아요를 할 수 있도록
       #article에 좋아요를 누른 user인지 아닌지 비교해야함 
       #article을 기반으로 좋아요버튼을 확인해야함
        if request.user in article.like_users.all():
            #좋아요를 누른 경우 -> 취소
            article.like_users.remove(request.user) #좋아요 취소
        else:
            article.like_users.add(request.user) #좋아요 추가 == 즉 게시글에 좋아요한 유저 추가
    return redirect('articles:index')
#작성자 본인은 좋아요를 하지 못하게 막았다.
