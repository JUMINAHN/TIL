from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class MyUserCreationForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model() #usermodel 호출

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()