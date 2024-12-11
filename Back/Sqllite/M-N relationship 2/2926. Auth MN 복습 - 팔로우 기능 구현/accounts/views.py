from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


from django.contrib.auth import logout as auth_logout


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


from django.contrib.auth.forms import PasswordChangeForm


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


from django.contrib.auth import get_user_model


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


from django.contrib.auth import get_user_model
@login_required #로그인만 가능 -> 로그인 되어있지 않을떄 로그인 페이지로 redirect?
# == 이거 자체가 자동으로 redirect 되는 것 -> 로그인 페이지로
#authenticated
#follow 기능 구현
def follow(request, username): #user에 대한 정보
    #로그인 되어있지 않다면 로그인 페이지로 redirect 되어야 한다. == authenticated -> html에서
    User = get_user_model()
    person = User.objects.get(username=username) #특정 유저가 본인과 같지 않은지 확인 #나의 입장
    if request.user != person:
    #자신을 follow할 수 없어야 함
    #내가 -> 그사람들 목록에 있는지
        if request.user in person.followers.all() : #목록에 있따면 -< 팔로우 취소 == 지금 여기서 활성화안됨
            person.followers.remove(request.user)
        else: #없다면
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username) #실제로 매개변수로 받은 내용을 사용할 수 있음
#person.username을 하면 데이터베이스에서 실제로 조회된 사용자이름 접근 가능 == 더 명확해짐
#나의 프로필 페이지가 아니라 그 사람의 페이지에
#팔로우 여부에 따라 다른 버튼이 렌더링

#profile