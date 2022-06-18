from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from .models import Profile

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):

    profile_pic = forms.ImageField(required=True)        
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'fullname'}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'locality'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    # lane_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'lane number'}))              

    class Meta:

        model = Profile
        fields = ['fullname', 'locality','profile_pic']
        exclude =['user']

# class EditProfileForm(forms.ModelForm):
#     image = forms.ImageField(required=True)
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}), required=True)
#     bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
#     location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}), required=True)

#     class Meta:
#         model = Profile
#         fields = ['image', 'first_name', 'last_name', 'bio', 'url', 'location']


