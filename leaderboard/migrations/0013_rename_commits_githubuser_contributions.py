# Generated by Django 3.2.4 on 2022-09-18 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0012_auto_20220918_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubuser',
            old_name='commits',
            new_name='contributions',
        ),
    ]
