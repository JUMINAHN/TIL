from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#password change

class CustomUserCreationForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomerUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
         model = get_user_model() #수정 기능 구현
         #수정에 fields에서 보이는 부분을 수정하지 않으면 불필요한 정보를 노출할 위험이 있따
         fields = ("first_name", "last_name",)
