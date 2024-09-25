#form은 모델에 대한 내용을 가져올 것
from django import forms #django forms -> django에서 form을 가져온다.
#reservation 호출
from .models import Reservation

#modelsForm 작성하기
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__" #모든 필드를 제공한다.
