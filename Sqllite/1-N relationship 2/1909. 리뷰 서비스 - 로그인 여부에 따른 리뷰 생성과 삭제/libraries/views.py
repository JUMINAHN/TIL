from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

#review form에 대한 정보를 추가할 것 -> 왜냐하면 review에대한 것을등록할 것이니까
def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all() #book에 대한 것으로 역참조 -> 리뷰 역참조
    review_form = ReviewForm()
    context = {
        'book': book,
        'review_form' : review_form,
        'reviews' : reviews
    }
    return render(request, 'libraries/detail.html', context)

#review_create
#review_create는 -> detail 페이지에서 -> book에 대한 정보를 바탕으로 이루어짐
def review_create(request, book_pk): #book정보
    book = Book.objects.get(pk=book_pk) #pk에 대한 정보
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book #review의 book -> book_instance == book에 대한 정보
        review.user = request.user #request에서 받아서 == user에 대한 정보 저장
        review_form.save() #다시 저장
        return redirect('libraries:detail', book_pk) #detail page로
    context = {
        'review_form' : review_form
#        'book' : book #book에 대한 정보
    }
    return render(request, 'libraries/detail', context)

#user에 대한 정보, review에 대한 정보 -> user ? review? 
#review를 삭제
def review_delete(request, book_pk, review_pk): #book_pk에 대한 정보를 받고 -> 그 뒤에 삭제
    #book = Book.objects.get(pk=book_pk) #book에 대한 정보를 받고 -> book이 아니라 review를 삭제할 것임
    #book의 review를 삭제,, 
    #삭제할 정보 -> review를 삭제할 것임
    review = Review.objects.get(pk=review_pk) #특정 리뷰 삭제
    if request.user == review.user : #위에서 request와 review의 유저가 같은가?
        review.delete() #같으면 review 삭제
    return redirect('libraries:detail', book_pk) #다시 상세페이지로 리턴