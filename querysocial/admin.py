from django.contrib import admin

# Register your models here.

from .models import SocialSite


class SocialAdmin(admin.ModelAdmin):

    list_display = ('site_name', 'site_base_url', 'site_suffix', 'site_user_id_suffix')




from .models import UserMaster

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name','user_artist_name')


from .models import UserSiteDetail

class UserSiteAdmin(admin.ModelAdmin):
    list_display = ('user_site_id','user_master','user_site_name',)



admin.site.register(SocialSite, SocialAdmin)
admin.site.register(UserMaster, UserAdmin)
admin.site.register(UserSiteDetail, UserSiteAdmin)

