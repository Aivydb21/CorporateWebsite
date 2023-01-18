
from django.urls import path , include
from django.conf import settings
from home.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home' ),

]