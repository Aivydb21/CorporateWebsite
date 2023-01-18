from utils import AdminImageWidget
from django.contrib import admin
from home.models import HomePageSlider
from django.db import models

class HomePageSliderAdmin(admin.StackedInline):
    extra = 1
    model = HomePageSlider
    list_display = [
        "id",
    ]
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
