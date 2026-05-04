from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from ..models import Videogame, Platform, VideogamePlatform
from ..services import get_videogame_details

def add_game(request):
    
    if request.method == "POST":
        #1. Retrieve the game_id from the POST parameters
        game_id = request.POST.get("game_id")
        #2. Save the information on the variable "result" by calling the get_videogame_details service with the game_id
        result = get_videogame_details(game_id)
        #3. Check if the title of the game already exists in the dabatabase. If it does note exists, it creates a new game with the retrieved information.
        with transaction.atomic():
            try:
                game_to_add, created = Videogame.objects.get_or_create(
                    title=result["name"],
                    defaults={"description": result["description"]}
                    )
                   
                #4. Check for all the platforms of the game.
                # If the platform does not exist in the database, it creates a new platform with the retrieved information.
                for platform in result["platforms"]:
                    if not Platform.objects.filter(name=platform["platform"]["name"]).exists():
                        platform_to_add = Platform.objects.create(
                            name=platform["platform"]["name"]
                        )
                    platform_to_add = Platform.objects.get(name=platform["platform"]["name"])
                    #5. Create a new VideogamePlatform object with the retrieved information.
                    if not VideogamePlatform.objects.filter(videogame=game_to_add, platform=platform_to_add).exists():
                        VideogamePlatform.objects.create(
                                        videogame=game_to_add,
                                        platform=platform_to_add,
                                        release_date=platform["released_at"]
                                    )         
            except Exception as e:
                print(e)
                messages.error(request, "The Videogame could not be created. Please try again.")
                return redirect("medialib:game.details", game_id=game_id)
    messages.success(request, "Game added successfully.")
    return redirect("medialib:home")

