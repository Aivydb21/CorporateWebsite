# Register your models here.
from django.utils.html import format_html
from django.contrib import admin
from django.db import models
from utils import AdminImageWidget

from .models import MissionPage
from utils import *



class MissionPageAdmin(admin.ModelAdmin):

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


    def logo_preview(self, obj):
        try:                 
            return format_html(
                '<img src="{}" style="max-width: 200px;"/>'.format(obj.image.url)
            )
        except:
            return '' 

    logo_preview.allow_tags = True
    logo_preview.short_description = "Image preview"


    def add_view(self, request, form_url='', extra_context=None):
        obj = MissionPage.objects.all().last()  
        if obj:
            return self.change_view(request, object_id=str(obj.id) if obj else None)
        else:
            return super(type(self), self).add_view(request, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):    
        return self.add_view(request)

admin.site.register(MissionPage,MissionPageAdmin)