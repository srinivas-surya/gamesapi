from django.urls import path
from .views import games_api_data, load_data, GameListCreateApiView, game_detail_view

urlpatterns = [
    path('games_api_data/', games_api_data, name="games"),
    path('load_games_api_data/', load_data, name="load_data"),
    path("games_list/",
         GameListCreateApiView.as_view(),
         name="games-list"),
    path("games/<str:matchDate>/",
         game_detail_view,
         name="game-detail"),
]