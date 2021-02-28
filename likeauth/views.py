from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import likedislike

# Create your views here.
def home(request):
    likedislik = likedislike.objects.all()
    return render(request, 'index.html', {'likedislik': likedislik})


def registerView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        createNewuser = User.objects.create_user(
            first_name= firstname,
            last_name= lastname,
            username= username,
            email = email,
            password = password,
        )
        createNewuser.save()
        return redirect('/login')

    return render(request, 'register.html')
    return render(request, 'register.html')

def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password=password
        )

        if authUser is not None:
            login(request, authUser)
            return redirect('/')
        else:
            messages.error(request,'INVALID CREDENTIALS')

    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')


def like(request, id):
    currentImage = likedislike.objects.get(id=id)
    currentUser = request.user
    for i in currentImage.like.all():
        if i == currentUser:
            currentImage.like.remove(currentUser)
            break
        else:
            for i in currentImage.dislike.all():
                if i == currentUser:
                    currentImage.dislike.remove(currentUser)
                    break
                else:
                    currentImage.like.add(currentUser)

    return redirect('/')

def dislike(request, id):
    currentImage = likedislike.objects.get(id=id)
    currentUser = request.user
    for i in currentImage.dislike.all():
        if i == currentUser:
            currentImage.dislike.remove(currentUser)
            break
        else:
            for i in currentImage.like.all():
                if i == currentUser:
                    currentImage.like.remove(currentUser)
                    break
                else:
                    currentImage.dislike.add(currentUser)

    return redirect('/')