from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.models import User

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': 'your username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'secret password'}))




class NewUserForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Computername'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Secret Password'
                }
            )
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
