from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Email',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password1=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password2=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Re-enter Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

class LogIn(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password1']
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

    