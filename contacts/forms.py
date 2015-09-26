from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 200, widget = forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 200, widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    repeat_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class NewContactForm(forms.Form):
    firstname = forms.CharField(label = 'First Name', max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}), required = True)
    lastname = forms.CharField(label = 'Last Name', max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control', 'notRequired': ''}), required = False)
    phone = forms.CharField(label = 'Phone', max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}), required = True)
