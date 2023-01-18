from django.contrib import admin
from utils import AdminImageWidget
from django.db import models
# Register your models here.
from contact.models import Contact, ContactUs ,ContactBanner


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'contacted_on')

    class Meta:
        verbose_name = "Contact Page"

class ContactBannerAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = ContactBanner
    list_display_links = ["id"]
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    class Meta:
        verbose_name = "Contact Banner"


class ContactUsAdmin(admin.ModelAdmin):

    extra = 1
    max_num = 1
    list_display = ['contact_us_title']

    inlines  = [ContactBannerAdmin]

    
    
    def add_view(self, request, form_url='', extra_context=None):
        obj = ContactUs.objects.all().last()  
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


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)



