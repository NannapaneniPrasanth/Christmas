from django import forms
class Hr_LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())




