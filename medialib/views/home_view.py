from django.shortcuts import render

def home(request):
    return render(request, "medialib/components/home.html")