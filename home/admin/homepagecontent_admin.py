from home.models import HomePageContent 
from .homepagefooter_admin import FooterAdmin
from .homepagehistory_admin import HomePageHistoryAdmin
# from .homepageservices_admin import HomePageServicesAdmin
from .homepageslider_admin import HomePageSliderAdmin
from .homepagevaluesandmission_admin import HomePageValueAndMissionsAdmin
from django.contrib import admin
from utils import AdminImageWidget
from django.db import models
from django.utils.html import format_html






    
     
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = [
        "id"
        
    ]
    list_display_links = ["id"]
    
    inlines  = [FooterAdmin, HomePageHistoryAdmin, HomePageSliderAdmin, HomePageValueAndMissionsAdmin ]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def add_view(self, request, form_url='', extra_context=None):
        obj = HomePageContent.objects.all().last()  
        if obj:
            return self.change_view(request, object_id=str(obj.id) if obj else None)
        else:
            return super(type(self), self).add_view(request, form_url, extra_context)
    def changelist_view(self, request, extra_context=None):
        return self.add_view(request)
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
admin.site.register(HomePageContent,HomePageContentAdmin)    
