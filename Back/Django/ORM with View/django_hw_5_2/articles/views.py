from django.shortcuts import render, redirect #redirect define 확인 -> 선언
from .models import Article #model 클래스를 가져와야 함.. #중요 --> 이것 오류

# Create your views here.
def index(request): #여러개를 받아와야하는 것? -> content 출력
    articles = Article.objects.all() #전체를 그냥 준다.
    context = {
        'articles' : articles
    }    
    return render(request, 'articles/index.html', context)

#데이터를 저장하고, redirect한다. 
#즉 요청을 받고 응답하는 형태
#새로운 것을 생성할 create 새로운 데이터 확인을 위한 new
#지금 상세페이지 조회가 아님
def new(request): #데이터 하나만 있어도 됨 -> 생성페이지로 돌려준다
    return render(request, 'articles/new.html')

def create(request): #form으로부터 정보를 받아와야 함
    #redirect한 것
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content) #받은 것을 저장 --> 이것 오류!!
    #데이터 저장
    article.save()  #제목과 내용.. 
    return redirect('articles:index') #뽑을 정보 -> html처럼 => articles 경로로 다시 리턴
    #pk 정보 삭제함 -> 못잡아냄
    #pk 정보를 기반으로