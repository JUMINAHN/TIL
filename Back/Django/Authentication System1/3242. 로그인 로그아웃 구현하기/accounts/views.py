from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout

# Create your views here.
def index(request): #전체 유저를 확인할 수 있는 페이지 구성
    #전체 유저 확인? -> 이전에는 models.all을했는데 동일하게 User?
    users = User.objects.all() #전체 유저 조회
    #form에 대한 정보도 전달해서 받아야 함 -> form data
    #이부분 유의할 것
    form = AuthenticationForm() #form에서 받은 정보를 반영할 수 있도록 해당 부분에 선언을 해줘야 함!!!
    context = {
        'users' : users,
        'form' : form,
    }
    return render(request, 'accounts/index.html', context) #accounts에 있는 index html

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            my_login(request, form.get_user()) #form에서 받아온 것에 대해 user 찾기
            return redirect('accounts:index') #mainpage로 돌려주기

    else : 
        form = AuthenticationForm()
    context = {
        'form' : form
    } #login을 할 수 있도록 page html 전달
    return render(request, 'accounts/login.html', context)

def logout(request):
    my_logout(request) #로그아웃 main으로
    return redirect('accounts:index')