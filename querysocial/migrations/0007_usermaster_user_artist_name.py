# Generated by Django 3.1.1 on 2020-10-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysocial', '0006_auto_20201009_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='user_artist_name',
            field=models.CharField(default='Artist Name', max_length=64),
        ),
    ]