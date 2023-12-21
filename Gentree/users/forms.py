from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from users.models import User
# from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'email')

    