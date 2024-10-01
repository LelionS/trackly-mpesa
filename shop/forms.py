from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False   
        if commit:
            user.save()
        return user

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, label="Enter OTP")

