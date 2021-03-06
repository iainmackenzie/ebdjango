# Generated by Django 3.1.1 on 2020-09-20 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=64)),
                ('site_base_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querysocial.socialsite')),
            ],
        ),
    ]
