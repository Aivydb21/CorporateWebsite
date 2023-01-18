from utils import AdminImageWidget
from django.db import models
from home.models import HomePageHistory
from django.contrib import admin

class HomePageHistoryAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = HomePageHistory
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}