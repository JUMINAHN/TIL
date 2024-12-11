from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request) : #그냥 지금은 -> 저자 전체 목록 확인할 수 있는 페이지 구성
    #저자..
    #지금 유의할 점이있는데 -> author.pk의 인자를 index에서 받아야하는데 활용할 수 없다는 점..
    authors = Author.objects.all()
    context = {
        'authors' : authors
    }
    return render(request, 'libraries/index.html', context)

#유저 정보 -> 상세정보를 돌려줄 것입니다. 
def detail(request, author_pk):
    #어디서? 게시글에 있는 디테일한 내용을 돌려받을 것입니다.
    author = Author.objects.get(pk=author_pk)#이 내용을 받을 것이고 -> 그걸 띄워줄 것입니다.
    context = {
        'author' : author
    } #detail 페이지에 돌려줄것입니다. == 일단은 
    #전반적인것 think
    return render(request, 'libraries/detail.html', context) #이걸 돌려줘야 함