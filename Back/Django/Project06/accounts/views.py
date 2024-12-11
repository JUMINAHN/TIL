from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
#from .models import User
from django.contrib.auth import get_user_model


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('boards:index')


#accounts에서 profile을 확인해야 함
def profiles(request, username): #link에서 받을 request내부와 username
    #이 username을 어떻게 할 것인가?
    #username과 관련된 페이지를 보여줘야 함 == 언제? 프로필 페이지를 눌렀을 때 == user의 정보를 가져와야 함
    User = get_user_model() #직접적인 호출 => 권고사항X
    person = User.objects.get(username=username) #username이라는 category에 username을 전달해준다.
    context = {
        'person' : person #이렇게 아닌데,,
    }
    return render(request, 'accounts/profile.html', context)

#이거는 post정보만 활용될 것
#팔로우 기능 구현 -> user이름 필요없음 pk정보 받아서 팔로우
def follows(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk) #person 정보 받았음
    #이 사람의 정보를 받아서 -> 팔로우 하는 것
    #관계를 추가하는 것 -> 일단 내가 그 사람이면 안돼
    if request.user != person: #같으면 안되고
        #같지 않다면 -> 이 유저들의 관계속에 내가 있는지 확인 => follower들의 목록
        if request.user in person.followers.all() : #이 팔로워들 안에 있다면 ==> 여기서는 메서드 호출하기!!
            #관계 해제
            person.followers.remove(request.user) #지운다.
        else :
            #관계 추가 => add를 해준다. => 그냥 기존에
            person.followers.add(request.user) #그냥 그 profile 페이지에
    return redirect('accounts:profiles', person.username) #그사람의 정보 == profile에는 name을 사용하니까