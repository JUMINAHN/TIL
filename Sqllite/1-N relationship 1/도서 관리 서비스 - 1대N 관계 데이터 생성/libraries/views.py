from django.shortcuts import render,redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request) : #그냥 지금은 -> 저자 전체 목록 확인할 수 있는 페이지 구성
    #저자..
    #지금 유의할 점이있는데 -> author.pk의 인자를 index에서 받아야하는데 활용할 수 없다는 점..
    authors = Author.objects.all() #authors가 쿼리셋임 => book_set은 author의 인스턴스에서만 가능
    #집필권수 -> author로 book의 정보를 출력해야 함 #역참조
    #book = Book()
    context = {
        'authors' : authors,
    }
    return render(request, 'libraries/index.html', context)

#유저 정보 -> 상세정보를 돌려줄 것입니다.
#상세 페이지에서 이제 저자를 참조하는 책의 제목을 모두 보여준다.
def detail(request, author_pk):
    #어디서? 게시글에 있는 디테일한 내용을 돌려받을 것입니다.
    author = Author.objects.get(pk=author_pk)#이 내용을 받을 것이고 -> 그걸 띄워줄 것입니다.
    book_form = BookForm()
    #저자의 내용을 -> 참조하는_set.에서 all찾는다
    books = author.book_set.all() #저자의 모든 책들을 저자를 통해서 찾았다. 
    context = {
        'author' : author,
        'book_form' : book_form,
        'books' : books
    } #detail 페이지에 돌려줄것입니다. == 일단은 
    #전반적인것 think
    return render(request, 'libraries/detail.html', context) #이걸 돌려줘야 함

#근데 상세 페이지에서도 -> 나의 form 칸을 받아오고
#보낸 요청에 따라서 -> post인 것들만 모아서
#그 세부정보를 나타낼 것
#도서 정보 생성 가능

#근데 이정보를 넣지 않으면..? 어떻게 article_pk를 가져와서 나의 데이터에 저장을 하지?
def books_create(request, author_pk): #airticle_pk에 대한 정보를 받는다 
    #if로 구분할 필요가 없음 post로만 받으니까 -> 데이터를 post로 받아온다.
    #기존과 동일
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm(request.POST) #requestPOST -> 이거에 대한 정보를 받았으니 유효성 검증이 진행되어야 함
    if book_form.is_valid():
        book = book_form.save(commit=False) #article에 대한 데이터를 보내줘야 함
        book.author = author #어떤 게시물에 관련된 것인지 받아야 하기 떄문임
        book_form.save()
        return redirect('libraries:detail', author_pk) #세부 데이터를 보여줘야하는데 그러한 인자가 없음 -> 여기에 이슈
    context = {
        'author' : author,
        'book_form' : book_form
    }
    return render(request, 'libraries/detail.html', context)
