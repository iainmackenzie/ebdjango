# Generated by Django 3.1.1 on 2020-09-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysocial', '0002_socialsite_site_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialsite',
            name='site_suffix',
            field=models.CharField(default='', max_length=64),
        ),
    ]
