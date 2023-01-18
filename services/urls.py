from django.urls import path , include
from django.conf import settings
from services.views import ServicesView

urlpatterns = [
    path('service/', ServicesView.as_view(), name='service' ),

]