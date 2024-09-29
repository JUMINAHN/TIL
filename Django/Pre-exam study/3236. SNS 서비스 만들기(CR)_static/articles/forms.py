#form을 사용할 것 -> 모델에서 정보를 받아올 것
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #article에서
    class Meta:
        model = Article
        fields = "__all__" #통해서 진행

