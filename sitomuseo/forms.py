from django import forms

class LoginForm(forms.Form):
    user_L = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'user'})
        )
    psw_L = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.PasswordInput(attrs={'placeholder':'password'})
        )

class SignupForm(forms.Form):
    user_S = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.TextInput(attrs={'placeholder':'user'})
        )
    psw_S = forms.CharField(
            label = '',
            max_length=100,
            widget = forms.PasswordInput(attrs={'placeholder':'password'})
        )