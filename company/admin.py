# Register your models here.
from django.utils.html import format_html
from django.contrib import admin
from django.db import models
from utils import AdminImageWidget

from .models import CompanyPage , CompanySectionOne , CompanySectionTwo , CompanySectionThree , CompanySectionFour,CompanySectionFive
from utils import *


class CompanySectionOneAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = CompanySectionOne
    list_display_links = ["id"]

    

class CompanySectionTwoAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = CompanySectionTwo
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

   
class CompanySectionThreeAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = CompanySectionThree
    list_display_links = ["id"]

    

class CompanySectionFourAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = CompanySectionFour
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

class CompanySectionFiveAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = CompanySectionFive
    list_display_links = ["id"]
class CompanyPageAdmin(admin.ModelAdmin):
    list_display = [
        "id"
        
    ]
    list_display_links = ["id"]
    
    inlines  = [CompanySectionOneAdmin , CompanySectionTwoAdmin , CompanySectionThreeAdmin , CompanySectionFourAdmin, CompanySectionFiveAdmin  ]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def add_view(self, request, form_url='', extra_context=None):
        obj = CompanyPage.objects.all().last()  
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
admin.site.register(CompanyPage,CompanyPageAdmin)    
