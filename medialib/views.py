from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm, AuthForm

def home(request):
    return render(request, "medialib/components/home.html")

def register(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, "Account created succesfully")
                return redirect ('medialib:login')
    return render(request, "medialib/user/create_user.html", {"form": form})

def login_view(request):
    if request.method == "GET":
        form = AuthForm()
    else: 
        form = AuthForm(request.POST)
        if form.is_valid():
            return HttpResponse("Login Saccsesfulíh")
    return render (request, "medialib/auth/login.html", {"form": form})
    