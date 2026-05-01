from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import RegisterForm

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

def dashboard(request, user_id):
    return render(request, "medialib/user/dashboard.html", {"user_id": user_id})