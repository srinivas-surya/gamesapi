from django.db import models

# Create your models here.


class MatchesData(models.Model):

    homeTeamName = models.CharField(max_length=100)
    homeTeamScore = models.IntegerField()
    awayTeamName = models.CharField(max_length=100)
    awayTeamScore = models.IntegerField()
    matchDate = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.homeTeamName

    class Meta:
        db_table = "matchesdata"






