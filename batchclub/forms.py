from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'signature_dish', 'profile_picture', 'location']
        profile_picture = forms.ImageField(label='My_Signature_Dish', required=False)
        labels = {
            'bio': 'Bio',
            'signature_dish': 'Signature Dish',
            'profile_picture': 'Signature Dish Picture',
            'location': 'Location'
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(label='My Signature Dish', required=False)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'signature_dish', 'profile_picture', 'location']