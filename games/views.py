from django.shortcuts import render
from games.requests_data import pl_match_data

# Create your views here.


def games_api_data(request):
    data = pl_match_data()
    return render(request, "games/games_data.html", {"games_data": data})


