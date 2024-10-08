#수정, 생성과 관련된 내용을 업데이트 해줘야함
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #생성과 수정 관련 내용을 수정해야함
#model을 가져와야함 -> get_user_model()을 통해서
from django.contrib.auth import get_user_model
#모델폼을 수정했던 것과 동일하게 

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()