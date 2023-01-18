from django.utils.html import format_html
from django.contrib import admin
from home.models import HomePageValueAndMissions
from utils import AdminImageWidget
from django.db import models

class HomePageValueAndMissionsAdmin(admin.StackedInline):
    extra = 1
    model = HomePageValueAndMissions
    list_display = [
        "id",
        
    ]
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}