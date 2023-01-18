from django.urls import path , include
from django.conf import settings
from ourclient.views import OurClients

urlpatterns = [
    path('our-client/', OurClients.as_view(), name='our-client' ),

]