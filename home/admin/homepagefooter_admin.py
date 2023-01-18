from django.contrib import admin
from home.models import Footer
from django.db import models
from utils import AdminImageWidget
class FooterAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Footer
    list_display_links = ["id"]
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}