from rest_framework import serializers
from games.models import MatchesData


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchesData
        # fields = "__all__" # we want all fields in the model
        # fields = ("author", "title") # we want to choose couple of fields
        exclude = ("id",)




