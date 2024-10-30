from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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

from django.http import JsonResponse

#좋아요 필터링 -> 좋아요를 했나요? : is_liked
#여기서 좋아요를 얼만큼했는지에 대한 데이터를 보내줘야 함 -> context내부에
@login_required
@require_POST
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        # if request.user in person.followers.all():
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_liked = False
        else:
            person.followers.add(request.user)
            is_liked = True
        context = {
            'is_liked' : is_liked,#if에 대한 결과값 => 여기에 followingNumber를 보내준다.
            'followingNumbers' : person.followings.count(), #이부분은 모델을 봐야할 것 같음 => 자체적으로 followings를 보유함 역참조가 followers
            'followersNumbers' : person.followers.count(), #여기는 메서드로 델꼬와야함
        } #if 조건문일 떄 수행 context => 해당 구문이 수행될 수 있는 이유는 자체적으로 profile내부에서 비동기 작업을 진행
        #좋아요 한 것에 따라 좋아요 취소 여부를 나타낼 수 있음 == 지금은 수행은 되지만 새로 고침을 해야 함
        #일단 중요한 것은 is_liked를 사용할 수 있음 => 무엇으로? response.data값으로 
        return JsonResponse(context) #따라서 js에서 is_liked 구문을 사용할 수 있음
    return redirect('accounts:profile', person.username)
