from home.models import HomePageNewsLetter
from django.contrib import admin

class HomePageNewsLetterAdmin(admin.ModelAdmin):
   list_display = ['email']

admin.site.register(HomePageNewsLetter,HomePageNewsLetterAdmin)   