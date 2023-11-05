from django import forms


class UserRegisterationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()