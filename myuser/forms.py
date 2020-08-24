from django import forms
from myuser.models import MyUser

class LogInForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    
class AddUserForm(forms.Form):
    display_name = forms.CharField(max_length=240)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)