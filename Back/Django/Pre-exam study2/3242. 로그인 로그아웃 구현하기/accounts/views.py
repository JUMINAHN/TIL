from django.shortcuts import render,redirect
from .models import User
#뭔가를 받아서 해야함 -> user와 관련된 form을 작성을 해야하는데 
#user을 받아와서 login 검증을 해야함

#form을 받아와야 함 == 일단 인증 관련 form이 있는지 확인
from django.contrib.auth.forms import AuthenticationForm #인증관련 form 존재 == 이것을 사용
from django.contrib.auth import login as my_login 
from django.contrib.auth import logout as my_logout
from django.contrib.auth import get_user

# Create your views here.
def index(request):
    #전체 유저 목록 확인
    users = User.objects.all()
    context = {
        'users' : users 
    }
    return render(request, 'accounts/index.html', context)

#login을 하기 위해서 get과 post로 생각
def login(request):
    if request.method == "POST":  
        form = AuthenticationForm(request, request.POST) #세션 정보를 위해서
        if form.is_valid(): #form에 정보를 기반으로 -> 유저 확인
            my_login(request, form.get_user()) #요청 == save대신 -> 진행
            return redirect('accounts:index') #login 페이지--> 여기로 가는게 아니라 index로
    else : 
        form = AuthenticationForm() #인증 폼
    context = {
        'form' : form
    } #인증 페이지로
    return render(request, 'accounts/login.html', context) #login을 해야하니까

def logout(request): #delete한것과 비슷함
    my_logout(request) #그냥 지금 로그인한 사용자 정보를 기반으로 -> 입력값X
    return redirect('accounts:index')