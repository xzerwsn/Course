from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your name'
        }),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'}),
            required=True
            )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter password',
            'label': 'Password'
        }),
        required=True,
        label= 'Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirm password',
        }),
        required=True,
        label= 'Confirm password'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter login',
    })
    )
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter password',
    }),
    required=True
    )

class ProfileForm(forms.ModelForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Username',
    })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
    }), required=True
    )

    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter phone number',
        })
    )
    github_url = forms.CharField(
        label="GitHub",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'GitHub URL',
        })
    )
    address = forms.CharField(
        label="Адрес",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter address',
        })
    )

    class Meta:
        model = Profile
        fields = ['username', 'email','github_url', 'phone_number', 'address']