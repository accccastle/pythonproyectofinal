from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=70, required=True)
    surname = forms.CharField(max_length=70, required=True)
    class Meta:
        model = User
        fields = ['username', 'name', 'surname','email','password1','password2']
        
