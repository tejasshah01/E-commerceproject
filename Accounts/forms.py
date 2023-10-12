from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import User


class sign_up(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter your First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter your valid Email id'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your 8 digit password'}))
    password2 = forms.CharField(label="Confirm_password",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    class Meta:
        model=User
        fields=["first_name","last_name","email","phone","password1","password2"]
        widgets={
            'phone':forms.TextInput(attrs={'placeholder':'Enter a Phone Number'})
        }

class User_login(forms.Form):
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your 8 digit password'}))