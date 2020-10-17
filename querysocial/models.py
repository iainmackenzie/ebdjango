from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class SocialSite(models.Model):
    site_name = models.CharField(verbose_name='Site Name', max_length=64)
    site_logo_url = models.CharField( verbose_name='Logo URL', max_length=128,default='')
    site_base_url = models.CharField(verbose_name='Site URL', max_length=200)
    site_suffix = models.CharField(verbose_name='Site Suffix', blank=True, max_length=64, default='')
    site_user_id_suffix = models.CharField(verbose_name='Site User ID Suffix', blank=True ,max_length=64, default='')
    def __str__(self):
        return self.site_name

class UserMaster(models.Model):
    user_first_name = models.CharField(max_length=64)
    user_last_name = models.CharField(max_length=64)
    user_artist_name = models.CharField(max_length=64, default='Artist Name')
    def __str__(self):
        return self.user_artist_name


class UserSiteDetail(models.Model):
    user_site_name = models.ForeignKey(SocialSite, on_delete=models.CASCADE)
    user_master = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    user_site_id = models.CharField(max_length=64)







