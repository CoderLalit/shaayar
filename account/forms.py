from django import forms
from models import *

class User(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('userid','username', 'name', 'email', 'password')