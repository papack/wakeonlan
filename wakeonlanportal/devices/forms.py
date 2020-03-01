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
                    'placeholder': 'ff:ff:ff:ff:ff:ff'
                }
            ),
            'desc' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'eg. Name of User'
                }
            )
        }
