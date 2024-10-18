# form 생성
# 회원 가입은 form을 생성해야 함
#from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #form 자체
from django.contrib.auth import get_user_model

#지금은 생성을 하면됨
class CustomUserCreationForm(UserCreationForm): #장고 기본적 -> 우리의 custom user를 바라보도록
    class Meta(UserChangeForm.Meta): #meta로 만들어져 있음 == Meta도 상속받으면 됨
        #model 속성을 제외하고는 모두 meta클래스 내용을 그대로 가져온다.
        model = get_user_model() #usermodel => 이거 ()메서드 사용하지 않아서 'function' object has no attribute '_meta'
        #함수 호출
        fields = "__all__" #fields도 == meat도

# class (UserChangeForm):
