from django.contrib import admin
from ourclient.models import ClientPageBanner, ClientPageSectionOne,ClientsHowItWorks, ClientPageSectionThree, \
 ClientPageSectionFour
from django.utils.html import format_html
from django.contrib import admin
from utils import AdminImageWidget
from django.db import models
# Register your models here.


class ClientPageSectionOneAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = ClientPageSectionOne
    list_display = [
        "id",
    ]
    list_display_links = ["id"]
    # readonly_fields = ["content_logo_preview"]
  


class ClientsHowItWorksAdmin(admin.StackedInline):
    extra = 1
    max_num = 50
    model = ClientsHowItWorks
    list_display = [
        "id", 
    ]
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


class ClientPageSectionThreeAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = ClientPageSectionThree
    list_display = [
        "id",
    ]
    list_display_links = ["id"]
    # readonly_fields = ["content_logo_preview"]
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}} 
class ClientPageSectionFourAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = ClientPageSectionFour
    list_display = [
        "id",
    ]
    list_display_links = ["id"]
    # readonly_fields = ["content_logo_preview"]   




class ClientPageBannerAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "title",
    ]
    list_display_links = ["id"]
    # readonly_fields = ["event_banner_preview"]
    inlines  = [ClientPageSectionOneAdmin,  ClientsHowItWorksAdmin, ClientPageSectionThreeAdmin ,  ClientPageSectionFourAdmin]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def add_view(self, request, form_url='', extra_context=None):
        obj = ClientPageBanner.objects.all().last()  
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
admin.site.register(ClientPageBanner,ClientPageBannerAdmin)      