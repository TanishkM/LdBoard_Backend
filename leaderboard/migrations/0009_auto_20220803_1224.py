# Generated by Django 3.2.4 on 2022-08-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0008_codechefuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='codechefuser',
            name='Country_rank',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='codechefuser',
            name='Global_rank',
            field=models.CharField(default='NA', max_length=10),
        ),
    ]