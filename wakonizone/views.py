from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile, Locality, Post
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/accounts/sign-in/')
def index(request):
    localities = Locality.objects.all()
    return render(request,'index.html',{'localities':localities})

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for { username }!!')
            return redirect('index')

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)   

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            messages.success(request,('You information is not valid'))
            return redirect('sign-in')

    else:
        return render(request,'sign-in.html')

def UserLocality(request, username):
    Locality.objects.get(user=request.user)
    user = get_object_or_404(User, username=username)

    locality = Locality.objects.get(username=username)
    profiles = Profile.objects.filter(username=username)

    context = {
      
        'locality': locality,
        'profiles': profiles

    }
    return render(request, 'locality.html', context)



def UserProfile(request, username):
   
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        
        'profile':profile
        
    }
    return render(request, 'profile.html', context)


