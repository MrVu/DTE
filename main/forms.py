from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')
