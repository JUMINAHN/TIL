from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
# gpt 도움받아서 개요만 보는중
def index(request):
    show_private = request.GET.get('show_private', False)
    
    if show_private:
        articles = Article.objects.filter(is_public=False)
    else:
        articles = Article.objects.filter(is_public=True)
    
    context = {
        'articles': articles,
        'show_private': show_private #조건부 랜더링을 위해서
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

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)