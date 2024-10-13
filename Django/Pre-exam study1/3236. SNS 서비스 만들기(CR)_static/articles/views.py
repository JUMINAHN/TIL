from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request): #요청 받아서 실행하려면 -> model의 전체 내용을 보여줘야 함
    articles = Article.objects.all() #모든 내용 확인하기
    context = {
        'articles' : articles
    } #index page로 보낼 것 -> data와 함께
    return render(request, 'articles/index.html', context)

#create의 기능을 한개로 구현
def create(request) :
    if request.method == "POST": #요청 메서드가 무엇인지?
        form = ArticleForm(request.POST, request.FILES) #이러한 데이터들 받아서 유효성 검사 후 활용
        if form.is_valid() : #유효성 검사에 통과되면 -> 저장
            form.save() #redirect 돌려준다. 메인으로
            return redirect('articles:index') #redirect로 돌려줌
    else : 
        form = ArticleForm() #해당 폼을 -> 보내줄 것
    context = {
        'form' : form
    } #new page로 보내준다.
    return render(request, 'articles/create.html', context) #생성 페이지로 다시 돌려준다.

def detail(request, pk):#요청받는다 -> 베리어블 라우팅을 통해 상세 내용을 요청받는다.
    article = Article.objects.get(pk=pk) #단일 -> 고유성을 위해 하나만 뽑음
    #그 내용에 대한것을 반환
    context = {
        'article' : article
    } #상세 페이지 반환
    return render(request, 'articles/detail.html', context) #context 내용 반환


#new -> form을 생성할 페이지를 제공
# def new(request): #request는 form이 있는 page로 전달 -> 따라서 form에 있는 데이터 양식을 받아와야 함
#     form = ArticleForm() #해당 폼을 -> 보내줄 것
#     context = {
#         'form' : form
#     } #new page로 보내준다.
#     return render(request, 'articles/new.html', context)

#해당 페이지의 특징은 랜더링해서 다시 메인 페이지로 보내주는 것 -> 전체 화면에서 잘 되어있는지 확인 가능
# def create(request): #form으로 POST로 요청받은 값, 그리고 사용자들이 업로드한 이미지 파일들을 db에 저장하고 응답
#     form = ArticleForm(request.POST, request.FILES) #이러한 데이터들 받아서 유효성 검사 후 활용
#     if form.is_valid() : #유효성 검사에 통과되면 -> 저장
#         form.save() #redirect 돌려준다. 메인으로
#         return redirect('articles:index')
#     #아니라면 유효성 검사가 이루어지지 않은 form이라면 -> 다시 new로 가서 form을 다시 작성하도록
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)