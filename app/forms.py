from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerRegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password (Again)",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}
