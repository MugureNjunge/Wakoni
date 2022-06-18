from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm, widgets
from .models import Profile, Business

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
  
    class Meta:

        model = Profile
        fields = ['fullname', 'locality','profile_pic']
        exclude =['user']

class NewBusinessForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}))
    business_image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Description'}), required=True)
    link = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Link'}), required=True)
    # Email


    class Meta:
        model = Business
        fields = ['business_image','title','description', 'link']
        




