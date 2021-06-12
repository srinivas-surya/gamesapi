from django.urls import path
from .views import games_api_data

urlpatterns = [
    path('games_api_data/', games_api_data, name="games")
]