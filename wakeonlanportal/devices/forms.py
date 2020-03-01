from django import forms
from .models import Device


class NewDeviceForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Device
        fields = ['name','mac','desc']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Computername'
                }
            ),
            'mac' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '1f2e3c4b5a6f'
                }
            ),
            'desc' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'eg. Name of User'
                }
            )
        }
