from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash #update-> hash ::
from django.contrib.auth.decorators import login_required
#비밀번호 업데이트해도 괜찮을 수 있도록
#form은 내장 되어있는 요소를 사용

User = get_user_model()

# Create your views here.
def index(request):
    persons = User.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
@login_required
def logout(request): #그냥 단순히 logout 해주면됨 -> login한것처럼
    auth_logout(request) #request받은 내용을 == post일 떄 수행,
    return redirect('accounts:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

#signupdate는 그냥 -> 기존 CRUD와 동일함
#다만, login은 request에 request post를 진행해야 함
#user.pk 정보는 => 비밀번호 변경을 할 때 이루어지고,
#여기서 특이하게 update를 할때는 그냥 새로운 정보만 받아옴 =>

#기존 정보를 받아오는 이유
#request 유저를 기반으로 == 수정 페이지와 동일함
#기존 정보 유지: 사용자의 기존 정보(이름, 이메일, 전화번호 등)를 폼에 미리 채워 넣기 위함
@login_required
def signupdate(request): #기존 유형에 동일 -> 수정 방식 동일
    if request.method == "POST": #현재 로그인한 사용자에 대한 세션을 관리하기 위해서
        form = CustomUserChangeForm(request.POST, instance=request.user) #그냥 사용자가 입력한 정보만 받아옴
        if form.is_valid():
            form.save() #다시 메인페이지로
            return redirect('accounts:index')
    else :
        form = CustomUserChangeForm(instance=request.user) #기존 정보를 받는게 아님 -> 업데이트를 위한 form page를 주는 것
        #만든 form => 유저 생성과 변경과 관련됨  
    context = {
        'form' : form
    } #signupdate페이지로 돌려줌 -> 기존 signup폴더로 돌려주는 것임
    return render(request, 'accounts/signupdate.html', context)

#view를 받아감 -> 기존 변경과 동일하나 이번에는 post로 받았을떄, 그리고 처음 login떄 했던것과 유사하게
#이전에는 단순히 request만 받았다면 이번에는 유저까지 같이 받는다.
@login_required
def change_password(request, user_pk) :
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST) #금번에는 form자체에서 get_user()를 했는데
        #여기서는 어떻게 왜 직접적으로 request.user을 하는 것인지
        #세션 자체에서 request를 하면 조회되었었는데 왜 여기서는??
        if form.is_valid():
            user = form.save() #main으로
            update_session_auth_hash(request, user) #form 정보에서 받은 user와 request 자체
            return redirect('accounts:index') #-> 메인페이지로 보내는게 아니라 세션업데이트
            
            #세션 업데이트를 위해 == request 사용
            #user는 form.save()로 반한된 사용자 객체 --> 새로운 사용자 객체 -> get.user()를 했었던 것 생각
            #즉 login에서 사용한 login 메서드와 구조적 역할과 동일한 매개변수로 생각하면 될 것 같음 == 내용은 다름
    else :
        form = PasswordChangeForm(request.user) #여기도 유저에 대한 정보를 그대로!! -> 저번처럼
    context = {
        'form' : form
    } #passwordpage
    return render(request, 'accounts/change_password.html', context)