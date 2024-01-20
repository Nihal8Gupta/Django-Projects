from django import forms
from django.contrib.auth.models import User
from app.models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
                   'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
                   'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}),}


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['address','pic']
        widgets={'address':forms.Textarea()}
        