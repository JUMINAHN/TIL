from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomerUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

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
def logout(request):
    auth_logout(request)
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

#회원정보 수정 기능 -> 기존처럼 동일함 : instance 받아와야 함
#상기 구조와 동일한 것을 볼 수 있음
@login_required
def signupdate(request):
    if request.method == "POST": #수정 페이지의 유무
        #update된 정보들
        form = CustomerUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index') #메인페이지로 다시 돌려준다.
    else : #form -> customer user == 회원정보 수정 -> 현재 회원의 정보
        form = CustomerUserChangeForm(instance=request.user) #instance를 가져와야 함
    context = {
        'form' : form
    }
    return render(request, 'accounts/signupdate.html', context) 

#비밀번호 변경 기능 구현
#    path('change_password/<int:user_pk>/', views.change_password, name="change_password"),
#그러면 동일하게 비밀번호 변경 form이 필요함 == 아마 내장?
#동일하게 업데이트 하는 것과 유사함 : 단 이거는 user정보를 받아서 지행해야 함
def change_password(request, user_pk):
    #user 정보...
    # user = User.objects.get(pk=user_pk)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST) #user먼저 받는 것
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index') #비밀번호 변경되었을 떄 -> 변동없이 만들기
    else : #음.. request로 ..? request.user랑 비교 해야할 것 같음
        #?? 
        form = PasswordChangeForm(request.user)#어떤 것? 유저 정보를 받아와야 함
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)
