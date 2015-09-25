from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 200, widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))
