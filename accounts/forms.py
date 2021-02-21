from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model  = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {
            'first_name': None,
            'last_name': None,
            'username': None,
            'email': None,
            'password1': None

        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class InstructorSignupForm(UserCreationForm):
    class Meta:
        model  = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff']
        help_texts = {
            'first_name': None,
            'last_name': None,
            'username': None,
            'email': None,
            'password1': None,

        }


    def __init__(self, *args, **kwargs):
        super(InstructorSignupForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class UserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['phoneNumber', 'userphoto' ]

