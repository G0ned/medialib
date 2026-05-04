from django.shortcuts import render, redirect
from ..services import search_videogames, get_videogame_details

def search_results(request):
    #TODO: Implement search results page
    #1. Retrieve the search query from the GET parameters of the request
    query = request.GET.get("search")
    #2. If the search query is empty, redirect the user to the home page
    if not query:
        return redirect("medialib:home")
    #3. If the search query is not empty, call the search_videogames service with the search query and render the search results
    results = search_videogames(query)
    return render(request, "medialib/components/search_results.html", {"result": results})

def game_details(request, game_id):
    #1. Retrieve the game_id from the URL parameters
    if not game_id:
        return redirect("medialib:home")
    results = get_videogame_details(game_id)
    return render(request, "medialib/components/videogame_details.html", {"game": results})