from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from ..models import Collection

def create_collection(request):
    if request.method == "POST":
        name = request.POST.get("name")
        with transaction.atomic():
            try:
                collection, created = Collection.objects.get_or_create(
                    name=name,
                    user=request.user
                )
            except Exception as e:
                print(e)
                messages.error(request, "The collection could not be created. Please try again.")
                return redirect("medialib:collection.create")
    else:
        return (render(request, 'medialib/collections/create_collections.html'))
    messages.success(request, "Collection created successfully!")
    return redirect("medialib:dashboard", user_id=request.user.id)