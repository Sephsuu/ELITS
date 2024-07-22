from django import forms
from .models import Students
# from .models import StudentProfile

class StudentCreationForm(forms.Form):
    email = forms.EmailField(
        max_length=255, 
        label='E-mail Address',
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'youremail@cvsu.edu.ph',
            'style': 'outline: 0.5px solid black;',
        }))
    password1 = forms.CharField(
        max_length=32, 
        label='Password',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'style': 'outline: 0.5px solid black;',
        }))
    password2 = forms.CharField(
        max_length=32, 
        label='Re-type Password',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'style': 'outline: 0.5px solid black;',
        }))

class StudentLogin(forms.Form):
    email = forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'style': 'outline: 0.5px solid black;',
            'placeholder': 'youremail@cvsu.edu.ph'
        }))
    password = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'style': 'outline: 0.5px solid black;',
        }))