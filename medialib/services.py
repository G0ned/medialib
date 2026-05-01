from decouple import config
import requests

API_KEY = config('RAWG_API_KEY')
#Service to search videogames using the RAWG API
def search_videogames(query):
    #TODO: Implement pagination and error handling
    #1. Definition of the base URL for the RAWG API
    url = f"https://api.rawg.io/api/games"
    #2. Send a GET request to the RAWG API with the query (retrieved from the search_form) and the API key as parameters
    response = requests.get(url, 
                        params={
                            "key": API_KEY,
                            "search": query,
                            "page_size": 10
                        })
    #3. Return the results of the search as a list of videogames or an empty list if there are no results
    return response.json().get('results', [])