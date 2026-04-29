from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from ..forms import AuthForm

def login_view(request):
    if request.method == "GET":
        #Call to the Authentication form class
        form = AuthForm()
    else: 
        form = AuthForm(request, data=request.POST)
        if form.is_valid(): #Check if the form is valid. It automatically chekcs if the username and password are correct.
            auth_user = form.get_user()
            if auth_user:
                login(request, auth_user) #Login the user
                messages.success(request, "Login succesfull!")
                return redirect('medialib:home') 
    return render (request, "medialib/auth/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        #Call to the logout function and logs out the current authenticated user
        logout(request)
        messages.success(request, "Logout succesfull!")
        return redirect('medialib:login')