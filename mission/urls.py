
from django.urls import path , include
from django.conf import settings
from mission.views import Mission

urlpatterns = [
    path('mission/', Mission.as_view(), name='mission' ),

]