from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'reg_form_input'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'reg_form_input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg_form_input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'reg_form_input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


