from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic

from querysocial.models import UserMaster, SocialSite, UserSiteDetail
from . import social_data as sd

user_artist_name = "extraocean"

def IndexView(request):
    template_name = 'querysocial/index.html'
    usersites = UserSiteDetail.objects.all()

    youtube_stats = ''
    instagram_stats = ''
    facebook_stats = ''
    contextlist = []
    for usersite in usersites:
        site_lookup = usersite.user_site_name_id
        site_record = SocialSite.objects.get(id=site_lookup)
        site_name = site_record.site_name
        site_url = site_record.site_base_url + site_record.site_suffix + usersite.user_site_id + site_record.site_user_id_suffix
 #       x_url, site_username = sd.search_site(site_record.site_base_url,user_artist_name)
        site_stats = sd.get_site_stats(site_name.upper(), site_url, usersite.user_site_id)
        contextlist += [{'uname': usersite.user_site_id, 'url': site_url, 'sname': site_name, 'stats': site_stats, 'logo': site_record.site_logo_url}]

    return render(request, template_name, context={"sites":contextlist})
