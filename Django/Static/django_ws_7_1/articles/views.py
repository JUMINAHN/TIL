from django.shortcuts import render,redirect
#article을 불러올 모델을 불러와야함
#form도
from .models import Article
from .forms import ArticleForm

# Create your views here.
# views는 def함수 선언을 통해 접근을 시도한다.
def index(request): #data를 줘야하기 떄문에
    #그런데 전체 목록 조회 기능을 구현한다고 했따.
    articles = Article.objects.all() #가져오고
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context) #index html에 주소를 돌려준다.

#create로 합치기
def create(request):
    if request.method == "POST": #요청 메서드
        form = ArticleForm(request.POST, request.FILES) #요청을 기반으로 받기 떄문에 -> form에서 다시 해야함
        if form.is_valid(): #유효하다면
            form.save() #저장하고 -> 맞으니까 메인 페이지로 돌려줘 -> redirect를 통해 다시 재요청
            return redirect('articles:index') #메인 페이지로
    else :
        form = ArticleForm() #폼 자체
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context) #돌려주고 저장할 것
    #왜냐하면 다시 생성을 해야하니까 메인페이지로 가면 안됨

def detail(request, pk): #request, 정보 받아오기 -> 디테일은 기존처럼
    article = Article.objects.get(pk=pk)
    #해당 내용을 가시화
    context = {
        'article' : article
    } #상세 페이지 이동
    return render(request, 'articles/detail.html', context) #detail


#urls로 new를 선언했다. -> 그런데 보면 forms를 사용한 것을 볼 수 있다.
#form 을 가져와서 사용할 것
# def new(request): #page로 보낼 것 -> form을 받아서 보낼 것
#     form = ArticleForm() #폼 자체
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context) #근데 form 데이터를 보낼 것

# # def create(request): #post받은 값을 이용해서 저장하고 -> 유효성 검사 진행해야 함
#     #이 생성할 떄 이번에는 파일을 올릴 수 있도록 post 옆에 FILES를 받아야함
#     form = ArticleForm(request.POST, request.FILES) #요청을 기반으로 받기 떄문에 -> form에서 다시 해야함
#     if form.is_valid(): #유효하다면
#         form.save() #저장하고 -> 맞으니까 메인 페이지로 돌려줘 -> redirect를 통해 다시 재요청
#         return redirect('articles:index') #메인 페이지로
#     #그게 아니면 다시 new로 돌려줘서 다시 작성하게 할 것
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/index.html', context) #돌려주고 저장할 것