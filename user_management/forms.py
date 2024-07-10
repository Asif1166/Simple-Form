from django import forms
from .models import UserManagment

class UserManagmentForm(forms.ModelForm):
    class Meta:
        model = UserManagment
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}))
