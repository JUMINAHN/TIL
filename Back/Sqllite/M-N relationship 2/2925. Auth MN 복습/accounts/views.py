from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
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
#profile과 관련됨
#profile에서는 유저 관련 정보를 제공할 것

def profile(request, username) : #유저의 정보
    User = get_user_model()
    #person = User.objects.get(pk=user_pk) #특정 유저의 정보
    person = User.objects.get(username=username)
    #특정 유저의 정보를 페이지로 돌려줄 것임
    context = {
        'person' : person,
    } #person정보를 돌려줌 -> 사람의 정보를 제공한다. 어디에? profile page에
    return render(request, 'accounts/profile.html', context)


# #하기는 팔로우 관련..!!
# #usermodel 가져오기 => get_user_model() : modelform이 아니니까
# from django.contrib.auth import get_user_model
# #view에서 랜더링 -> 
# def profile(request, user_pk): #유저를 기반으로 profile을 조회해야하기 때문에
#     #pofile에 대한 정보를 보내줘야 함
#     #user에 대한 정보를 조회하기 위해선? Usermodel에서 정보를 가져올 수 있어야 함
#     User = get_user_model() #user model로 -> user 조회
#     person = User.objects.get(pk=user_pk) #user 정보 받아오기 
#     #받아온 유저와 현재 로그인된 유저가 같은지? -> 같다면 자기한테 팔로워를 걸 수 없게 해야 함
#     #그리고 다르다면 다른 유저를 팔로우했는지 안했는지에 대한 조건을 명시하고 자것애햐 함
#     if person != request.user : #깥지 않을 경우 -> 로그인된 유저가 같지 않을 경우
#         #팔로우를 할 수 있도록하며 -> 팔로우 목록을 확인한다
#         #내가 팔로우했는지 -> 이사람 팔로우 리스트에 있는지 확인해야 함
#         if request.user in person.followers.all() :
#             person.followers.remove(request.user) #delete가 아니라 remove 사용해야 함
#             #리스트 안에 있다면 -> 팔로우 취소
#             #없다면 팔로우 
#         else:
#             #역으로 팔로우 신청 가능
#             person.followers.add(request.user)
#             #왜 username을 하는지 궁금함
#     return redirect('accounts:profile', person.username) #특정 사람의 화면이니까 user_pk??
#     #redirect profile로 보낸다 -> 프로필 화면에서 정보를 조회애햐하니까,,
#     #근데 왜 redirect르 할까?