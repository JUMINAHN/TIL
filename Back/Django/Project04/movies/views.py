from django.shortcuts import render, redirect
from .models import Movie
#form 데이터 받아오기
from .forms import MovieForm

# Create your views here.
def index(request): #전체 all로 받아오기
    movies = Movie.objects.all() #받아서 -> 보내준다..화면에 띄울 것
    context = {
        'movies' : movies #역시 오탈자 때문
    }
    return render(request, 'movies/index.html', context) #cotent를 받았으니까

def create(request):
    if request.method == "POST": #요청 메소드가 
        form = MovieForm(request.POST, request.FILES) #file? files? #request.FILES 곧 등록할 것
        #form을 받아서 유효성 검사를 진행할 것
        if form.is_valid():
            form.save() #검사에 성공하며 save하고 메인 화면으로 redirect
        return redirect('movies:index') #index로 돌려주고
    else:
        form = MovieForm()
    context = {
        'form' : form
    } #생성 페이지로 보내주기
    return render(request, 'movies/create.html', context)

def detail(request, pk): #detail 상세페이지 -> html로 보내기 -> 받은 detail의 세부 내용
    #pk는 괜찮음
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie #내용 확인
    }
    return render(request, 'movies/detail.html', context)

#삭제
def delete(request, pk): #삭제 특정 값 -> 수정/업데이트가 아니기 떄문에
    movie = Movie.objects.get(pk=pk) #pk값 삭제해서
    movie.delete() #redirect로 돌아간다. 
    return redirect('movies:index') #index page로

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":  
        form = MovieForm(request.POST, request.FILES,  instance=movie) #instance -> 요거만 검토하면 됨
        #이것도 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('movies:create') 
    else :
        # movie = Movie.objects.get(pk=pk) #movie에 대한 데이터
        form = MovieForm(instance=movie) #form에서 다시 돌아가 -> 수정 페이지 기존과 비슷하게 만들 것 -> instance 사용 이거 몰라
    context = {
        'movie' : movie,
        'form' : form
    }
    return render(request, 'movies/update.html', context) #수정하는 곳으로 정보를 보낸다.


#수정하기 -> edit page를 생성해서 만들기 
#기존 데이터 form에서 정보받아와서 세이브하기 -> 바꾸고
# def edit(request, pk): #여기서 post로 요청받아서 똑같이 진행할 것인데 -> 일단 이건 form을 가져오는 것
#     #그리고 기존 데이터를 가져올 것임
#     #그런데 기준 데이터를 기반으로 가져올 것
#     movie = Movie.objects.get(pk=pk) #movie에 대한 데이터
#     form = MovieForm(instance=movie) #form에서 다시 돌아가 -> 수정 페이지 기존과 비슷하게 만들 것 -> instance 사용 이거 몰라
#     context = {
#         'movie' : movie,
#         'form' : form
#     }
#     return render(request, 'movies/edit.html', context) #수정하는 곳으로 정보를 보낸다.

# def update(request, pk): #form에 정보 POST로 받아와서 update하고 랜더링
#     movie = Movie.objects.get(pk=pk)
#     form = MovieForm(request.POST, request.FILES,  instance=movie) #instance 
#     context = {
#         'movie' : movie,
#         'form' : form,
#     }
#     return redirect('movies:create', pk) #pk를 기반으로


#페이지 생성form으로 정보받아오기
# def new(request):
#     form = MovieForm()
#     context = {
#         'form' : form
#     } #생성 페이지로 보내주기
#     return render(request, 'movies/new.html', context)

# #form에서 post정보를 form으로 받아와서 받아서 사용할 것임
# def create(request): #단 여기서 request 파일도 받아올 것이고, post값도 받아올 것
#     form = MovieForm(request.POST, request.FILES) #file? files? #request.FILES 곧 등록할 것
#     #form을 받아서 유효성 검사를 진행할 것
#     if form.is_valid():
#         form.save() #검사에 성공하며 save하고 메인 화면으로 redirect
#         return redirect('movies:index') #index로 돌려주고
#     context = { #아니라면 context에 담아서 다시 -> 생성 페이지로 들어가자
#         'form' : form
#     } #movie.new 생성 페이지로 다시 보내준다.
#     return render(request, 'movies/new.html', context)