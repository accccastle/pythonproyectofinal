from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from users.models import UserProfile

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=70, label='Nombre', required=True)
    last_name = forms.CharField(max_length=70, label='Apellido', required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class UpdateForm(UserChangeForm):
    username = forms.CharField(max_length=100, required=True, label='Usuario')
    first_name = forms.CharField(max_length=70, label='Nombre', required=True)
    last_name = forms.CharField(max_length=70, label='Apellido', required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'phone', 'email', 'social_media', 'avatar']
