from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect('accounts:index')
    else :
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

#회원 가입 등록 폼을 따로 생성해야 함 -> USER기본 모델 변경 
#이것역시 요청+응답 :: 생성과 수정
#이게 create랑 정말 비슷했음
def signup(request) : #request 정보
    if request.method == "POST":
        form = MyUserCreationForm(request.POST) #request 정보를 받아서 -> 등록
        if form.is_valid():
            form.save() #등록
            return redirect('accounts:index')
    else :
        form = MyUserCreationForm() #회원 가입 form 제공
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)