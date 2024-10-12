#리뷰 form 작성
from django import forms
from .models import Book, Review

#form
class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ("content",) #content만 표시
