# Generated by Django 3.1.1 on 2020-10-09 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querysocial', '0005_socialsite_site_channel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=64)),
                ('user_last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserSiteDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_site_id', models.CharField(max_length=64)),
                ('user_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querysocial.usermaster')),
                ('user_site_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querysocial.socialsite')),
            ],
        ),
        migrations.DeleteModel(
            name='UserUrls',
        ),
    ]
