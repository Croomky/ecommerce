from django import forms

class SigninForm(forms.Form):
    login = forms.CharField(label='Username or email', max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))