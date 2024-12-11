from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods #view에 있는 decorations
from .forms import CustomUserCreationForm
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout
from django.contrib.auth import get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import update_session_auth_hash #decorator -> hash 값

#login 안해도 가능
#post 로그인 사용자만 가능

# Create your views here.
# 기능 완성 -> 테스트
#AttributeError: module 'accounts.views' has no attribute 'signup'
@require_http_methods(['GET', 'POST'])
def signup(request): #회원가입 정보 -> 오타
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) #정보를 받아와서 생성 => 정보만 받아서
        if form.is_valid(): #유효하다면
            form.save() #저장 -> db에 저장
            # update_session_auth_hash() #hash정보 == 비밀번호 변경
            my_login(request, get_user) #회원가입과 동시에 로그인
            #my_login(request, get_user) #요청과 - 활성화된 유저정보 받아오기
            #main화면으로
            return redirect('boards:indedx')
    else :
        form = CustomUserCreationForm() # 처음에는
    context = {
        'form' : form #form 정보를 받아서
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST) #session
        if form.is_valid():
            my_login(request, get_user)
            #next가 있다면 next로 보내라 라고 하는 것 ==> login.html 자리 비운이유
            next_url = request.GET.get('next') #??????????? == 바로 생성페이지로 갈 수 있도록 구현 
            #QQQQQQQQQQQQQQQQQ
            #?로 오는것 request랑 관련되기 떄문에 get에 있더라
            #없다면 none반환
            if next_url :
                return redirect(next_url)
            return redirect('boards:indedx')
    else :#만들어 놓은 것 가져다 쓰면 됨
        form = AuthenticationForm() #어떻게 바로? -> 특정 필드를 받고 싶을때 == db정보 == .FORM은 모델 필드 외의 데이터도 입력이 가능하다.
    context = {
        'form' : form
    }
    return(request, 'accounts/login.html', context)


@require_http_methods(['POST']) #요청만
@login_required #밑과 위에 대한 차이? == 순서가 있다. -> post요청하고 login 
def logout(request):
    my_logout(request) 
    return redirect('boards:indedx')