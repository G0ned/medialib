from django.urls import path
from django.conf import settings
from . import views

app_name = "medialib"

urlpatterns = [
    path("", views.home, name="home"),
    path("user/create", views.register, name="create.user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"), 
    path("dashboard/<int:user_id>", views.dashboard, name="dashboard"),
    path("search-results", views.search_results, name="search.results"),
    path("game-details/<int:game_id>", views.game_details, name="game.details"),
    path("add-game", views.add_game, name="add.game"),
]