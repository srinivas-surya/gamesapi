from django.shortcuts import render, HttpResponse
import requests
from .models import MatchesData

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from games.api.serializers import GameSerializer
from games.api.pagination import SmallPagination


# Create your views here.

# generic concrete view
class GameListCreateApiView(generics.ListAPIView):
    queryset = MatchesData.objects.all().order_by("-matchDate")
    serializer_class = GameSerializer

    pagination_class = SmallPagination


@api_view(["GET"])
def game_detail_view(request, matchDate):
    try:
        article = MatchesData.objects.filter(matchDate=matchDate)
        print(article)
    except MatchesData.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "game not found",
        }
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GameSerializer(article, many=True)
        return Response(serializer.data)


def games_api_data(request):
    data = MatchesData.objects.all()
    return render(request, "games/games_data.html", {"games_data": data})


def load_data(request):

    url = 'https://api.football-data.org/v2/competitions/PL/matches'

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url,  headers={"X-Auth-Token": "6c0769f154324085b5a595a887d82377"})

    data = (x.json())

    new_data = []

    print("======= collecting foot ball api data ======")
    for key, value in data.items():
        if key == "matches":
            for i in value:
                date_ = (i["utcDate"])
                new_date = date_[0:10]
                new_data.append((new_date, i["homeTeam"]["name"], i["score"]["fullTime"]["homeTeam"],
                                 i['awayTeam']["name"], i["score"]["fullTime"]["homeTeam"], i["status"]))
    print(len(new_data))

    print("========= collecting ball api ===================")
    r = {"per_page": 100}
    new_list = []

    for page in range(1, 30):

        url = "https://www.balldontlie.io/api/v1/games/?seasons[]=2019/&per_page=40&page=" + str(page)
        x = requests.get(url)

        json_data = x.json()
        for i in json_data.get("data"):
            date_var = (i["date"])
            new_date_var = date_var[0:10]
            new_list.append((new_date_var, i["home_team"]['full_name'], i['home_team_score'],
                             i['visitor_team']['full_name'], i['visitor_team_score'], i["status"]))
    print(len(new_list))
    new_data.extend(new_list)

    for match_date, home_name, home_score, visitor_name, visitor_score, status in new_data:
        meal_data = MatchesData(
            homeTeamName=home_name,
            homeTeamScore=home_score,
            awayTeamName=visitor_name,
            awayTeamScore=visitor_score,
            matchDate=match_date,
            status=status
        )
        meal_data.save()

    return HttpResponse("data loaded")