from django import forms

class SigninForm(forms.Form):
    login = forms.CharField(label='Username or email', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())