from django import forms
from .models import Movie #movei에 대한 모델 -> 일반 호출 -> 오탈자 주의
#model을 기반으로 불러와야 함

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie #movie 진행
        fields = "__all__"
