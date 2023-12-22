from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ImageUploadForm
import os.path

from .models import *

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
    user_profile = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            user_profile.delete_old_image()
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserProfileForm(instance=request.user)
    context =  {'form': form}
    return render(request, 'profile.html', context)

# @login_required

def gallery(request):
    images = UserGallery.objects.filter(user_profile__user=request.user)
    return render(request, 'gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user_profile = request.user.userprofile
            image.save()
            return redirect('users:gallery')
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def delete_image(request, image_id):
    image = UserGallery.objects.get(pk=image_id)
    image.delete()

    # Удаление с диска
    if image.images:
        image.images.delete()

    # Так как, команда, удаляющая с диска генерирует в БД запись с пустым путем, зачищаем её
    last_object = UserGallery.objects.latest('id')
    last_object.delete()

    return redirect('users:gallery')