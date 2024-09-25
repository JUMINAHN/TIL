#forms.py에서 modelform을 작성하기 위해선 form을 호출해야하고 == 같은 내부 로직안에 있음
#form에 대한 모델도 호출해야한다. 
from .models import Memos #memods라는 모델을 부를것이고
from django import forms #장고 자체에서 forms라는 것을 사용할 것이다.

#model class에서 작성한것처럼 동일하게 진행
class MemosForm(forms.ModelForm): #model에 특정속성에 접근을 해야함
    summary = forms.CharField(
        label = "Summary",
        widget= forms.TextInput(
            attrs= {
                'placeholder' : 'summary',
            }
        ),
    )
    memo = forms.CharField(
        label = "Memo",
        widget= forms.Textarea(
            attrs= {
                'placeholder' : 'memo', #아 여기 오류 오탈자 유의
                'rows': 5,
                'cols': 50, 
            }
        )
    )

    class Meta:
        model = Memos
        fields = "__all__" #모든 데이터를 보여줄 것이기 떄문에
        #지금 위젯을 설정을 해줘야할 것 같음 -> memos가 너무 크게 나옴
        #summary 부분도 위젯을 설정해줘야할 것 같음
        
