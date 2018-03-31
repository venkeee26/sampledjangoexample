from djangolevelfive_app.models import Userprofileinfo
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class Userprofileinfo_form(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('website','profile_pic')
