# Generated by Django 3.2.4 on 2021-06-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchesdata',
            name='awayTeamScore',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matchesdata',
            name='homeTeamScore',
            field=models.IntegerField(),
        ),
    ]
