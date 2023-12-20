from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def UserLoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                pass
    else:
        form = UserLoginForm()
    context =  {'form': form}
    return render(request, 'login.html', context)

def UserRegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context =  {'form': form}
    return render(request, 'register.html', context)

def UserProfileView(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserProfileForm()
    context =  {'form': form}
    return render(request, 'profile.html', context)
