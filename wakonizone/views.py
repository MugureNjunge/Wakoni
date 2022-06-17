from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from django.contrib.auth.models import User
from .models import Profile
# from .forms import EditProfileForm, UserRegisterForm
from django.urls import resolve

def UserProfile(request, username):
   
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        
        'profile':profile
        
    }
    return render(request, 'profile.html', context)