# Generated by Django 3.2.4 on 2023-01-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0022_leetcodeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernames',
            name='ol_uname',
        ),
    ]