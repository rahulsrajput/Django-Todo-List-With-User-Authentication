from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class loginForm(AuthenticationForm):
    pass

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']