from django.urls import path , include
from django.conf import settings
from contact.views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact' ),

]