#auth의 create관련 model과 update관련 모델
#새로운 form 생성
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model #user model을 통해서 객체 받아오기

# .forms할필요가 없음
class MyUserCreationForm(UserCreationForm): #forms.UserCreationForm
    class Meta(UserCreationForm.Meta): #이런느낌? #메타상속..? 메타 부르기
        model = get_user_model() #사용자 기반으로 == 함수 호출을 해야 함!!
        #fields = ("Username", "Password",)
        #signup에는 별도 필드를 설정할 필요가 없음..!
        #meta만 특수하게 sth.META상속

#AttributeError: 'function' object has no attribute '_meta'

# class Form(forms.ModelForm):
#조금 다른 느낌    
#     class Meta:
#         model = 
#         fields = ("",)
