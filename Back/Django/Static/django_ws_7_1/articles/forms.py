#form 자체를 사용하고자 하고 -> forms를 부르고
#model 자체를 사용하고자 하고 -> models를 부른다.
from django import forms #django에 있는 기능
from .models import Article #aritlce 모델 부르기

#form tag 만들기 -> models form인지, 일반 form인지 == models form (Data 접근)
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__" #전체 조회
