from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'user'})
        )
    psw = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'password'})
        )

class SignupForm(forms.Form):
    user = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'user'})
        )
    psw = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'password'})
        )