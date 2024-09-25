from django import forms
#모델을 기반으로 modelform을 만들 것
from .models import Travels 

class TravelsForm(forms.ModelForm): #어떤 타입인지 생각
    location = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '제주도'        
            }
        )
    )
    start_date = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '2022-02-02'
            }            
        )
    )
    end_date = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '2022-02-02'
            }
        )
    )
    class Meta:
        model = Travels #이렇게 진행할 것
        fields = "__all__"
