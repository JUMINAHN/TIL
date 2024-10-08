from django.shortcuts import render, redirect
from .models import User
#login과 관련된 내용을 위해서는 현재 request상의 user를 가져와야 함
#그리고 auth == 인증 == 로그인과 관련된 form을 불러와야 함
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user #user 자체를 가져오는 것 -> usermodel을 가져오지 않음
#user model은 추 후 회원 가입 로직에서 사용될 것 
from django.contrib.auth import login, logout
#로그인과 관련된 속성 진행하면 됨
from .forms import MyUserChangeForm, MyUserCreationForm


# Create your views here.
# user model을 사용할 것
def index(request):
    #유저에 대한 정보를 사용해야 함
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context) #이구조도 나중에 이해해보자

#login과 관련된 form 생성 -> 로그인 정보를 주고, 받아야 함
#기존의 new, create와 비슷한 구조를 띔 
#다만 session 정보를 받아야하기 떄문에 request 구조를 다시 한 번 더 사용해야하는 부분이 차이점
#즉 기존의 CRUD 구조와 유사하게 진행 됨
def my_login(request):
    if request.method == "POST": #post인가 아닌가에 따라서 -> DB 정보를 저장하고 전송하겠습니다.
        form = AuthenticationForm(request, request.POST) #session과 사용자의 정보를 받습니다. -> 그리고 유효성 검증
        if form.is_valid(): #login을 할 수 있도록 해야함
            login(request, form.get_user()) #세션, 그리고 현재 form에서 받아지는 사용자의 현 정보 -> 로그인 시키고 -> 메인 페이지로 돌려준다.
            return redirect('accounts:index')
    else : #사용자의 요청값 -> get : 정보를 조회하겠습니다. => 즉 login과 관련된 정보를 사용해야 함
        form = AuthenticationForm()
    context = {
        'form' : form
    } #화면을 보여주세요 -> form화면을 보여주세요
    return render(request, "accounts/login.html", context)

#동일 -> 등록전에 새롭게 userform양식을 재정의해서 사용해주어야 함
#왜냐하면 메타 자체의 속성이 반영이 되지 않았기 떄문에
#등록은 기존과 동일하게 작용됨
def signup(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST) #post 정보를 받음 -> 기존에는 files정보까지 받았는데 이부분에선 필요가 없음
        if form.is_valid():
            form.save() #맞다면 저장하고 -> 돌려줌 -> DB에 저장 -> 상기는 인증수단 이거는 다름
            return redirect('accounts:index')
    else :
        form = MyUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)
