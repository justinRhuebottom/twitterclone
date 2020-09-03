from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    display_name = forms.CharField(max_length=30)
    email = forms.EmailField(widget=forms.EmailInput, max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)