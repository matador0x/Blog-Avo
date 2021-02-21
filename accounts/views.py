from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("blog:post_list")
        else:
            messages.warning(request, 'Username or password is wrong.')
    return render(request, 'accounts/login.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myprofile = profileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    context = {
        "userForm": userForm,
        "profileForm": profileForm,
    }
    return render(request, 'accounts/profile_edit.html', context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, 'accounts/register.html', context)


def userLoggedout(request):
    logout(request)
    return redirect('blog:post_list')
