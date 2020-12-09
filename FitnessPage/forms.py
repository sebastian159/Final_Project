from django import forms
from .models import Goals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class GoalForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']