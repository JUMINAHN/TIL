from django.shortcuts import render, redirect
from .models import User #models.py파일에서 User 모델을 가져오는 import 문법
#models.py == .models 현재 패키지 == 즉 현재 디렉토리의 models.py파일을 의미한다.
#models.py에 정의된 User class를 가져온다.
from django.contrib.auth import get_user #auth module에서 제공하는 인증 관련 함수 
#django contrib는 django에서 제공하는 추가적인 기능을 모아놓은 패키지
#auth는 contrib패키지 내의 인증관련 모듈 -> 사용자 계정, 그룹, 권한, 쿠키 기반 사용자 세션 등을 처리 함
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #이거는 생성, 수정 -> 회원가입?
#user는 -> 새로 재정의 해야함 -> 따라서 forms에서 다시
from .forms import MyUserChangeForm

#인증 자체
from django.contrib.auth.forms import AuthenticationForm #인증 관련 form -> 그냥 각 구조가 다른 것에 접근하는 것 뿐
# 사용자 인증 전문화, 세션 관리 용이 
from django.contrib.auth import login

# user model에서 user에 관련된 데이터를 받아옴
# user라는 model 에서 all 모든 정보를 받아옴
# Create your views here.
def index(request): 
    users = User.objects.all() #user의 전체 유저 목록을 확인할 수 있는 페이지 받아옴
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context) #유저에 대한 정보를 전송해줌 -> views
#user 정보를 준다.

#login은 기존 create와 동일한 구조를 띈다. -> 다만 약간의 성격이 다름
#일단 login,, 
#그 유저에 대한 정보를 얻으려면 get_user()? == 현재 로그인한 사용자의 정보를 가져올 떄 
def my_login(request): #login정보를 받음 -> request자체에 user의 정보가 들어있음
    if request.method == "POST": #유효성 검증 ==> 특이하게 post를 받고, request도 받음
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid(): #유효하다면 로그인 -> login method 호출
            login(request, form.get_user()) #login했으니까 redirect로 메인페이지 ##이 파트 
            return redirect('accounts:index')
    else : #post가 아닐때 -> get으로 정보를 받아올 떄 -> 단순 form으로 요청을 보내고자 할 때
        #정보를 받아오는 것임 -> 어디서? UserForm에서 : userform은 form을 생성할 필요가 없x..? 
        form = AuthenticationForm()
    context = { #login에 실패했을떄도 다시 이쪽으로 보내주기 위해서
        'form' : form
    }
    return render(request, 'accounts/login.html', context) #form에 대한 정보를 보냄

def signup(request): #기존 crud -> creat와 동일한 방식
    if request.method == "POST":
        form = MyUserChangeForm(request.POST) #단순 post받고 -> 그냥 단순 회원 가입 생성
        if form.is_valid():
            form.save() #기존과 동일
            return redirect('accounts:index')
    else :
        form = MyUserChangeForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)