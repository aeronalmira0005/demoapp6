from django import forms
from django.http.response import FileResponse

class entryForms(forms.Form):
    # LOGIN FORM
    input_username = forms.CharField(label="Username", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Username',
                                        'class': 'form-control',
                                     }))
    input_password = forms.CharField(label="Password", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'type': 'password',
                                     }))

    # REGISTRATION FORM
    first_name = forms.CharField(label="First Name", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'First Name',
                                        'class': 'form-control',
                                     }))
    last_name = forms.CharField(label="Last Name", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Last Name',
                                        'class': 'form-control',
                                     }))
    email = forms.EmailField(label="Email", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Email',
                                        'class': 'form-control',
                                     }))
    username = forms.CharField(label="Username", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Username',
                                        'class': 'form-control',
                                     }))    
    password1 = forms.CharField(label="Password", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'type': 'password',
                                     }))
    password2 = forms.CharField(label="Confirm Password", required=True,
                                     widget=forms.TextInput(attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control',
                                        'type': 'password',
                                     }))               