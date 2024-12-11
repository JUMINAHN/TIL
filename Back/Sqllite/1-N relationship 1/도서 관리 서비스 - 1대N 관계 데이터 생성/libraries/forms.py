from .models import Book
from django import forms #django 자체의 기능 -> contrib, conf가 아닌 단순 장고

#form을 생성할 떄 호출해줘야 함
class BookForm(forms.ModelForm): #책 정보 생성이 완료되면 -> 저자 상세 정보 페이지에 redirect
    class Meta:
        model = Book
        fields = ("title", "description", "adult", "price",)
