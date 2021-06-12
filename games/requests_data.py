import requests


def pl_match_data():
    url = 'https://api.football-data.org/v2/competitions/PL/matches'

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url, headers={"X-Auth-Token": "6c0769f154324085b5a595a887d82377"})

    data = (x.json())

    new_data = []

    print("======= collecting foot ball api data ======")
    for key , value in data.items():
        if key == "matches":
            for i in value:
                date_ = (i["utcDate"])
                new_date = date_[0:10]
                new_data.append([new_date,i["homeTeam"]["name"], i["score"]["fullTime"]["homeTeam"],
                i['awayTeam']["name"], i["score"]["fullTime"]["homeTeam"], i["status"]])
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
            new_list.append([new_date_var, i["home_team"]['full_name'], i['home_team_score'],
                             i['visitor_team']['full_name'], i['visitor_team_score'], i["status"]])
    print(len(new_list))
    new_data.extend(new_list)

    print(len(new_data))

    return new_data











