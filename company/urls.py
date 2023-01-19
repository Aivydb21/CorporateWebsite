
from django.urls import path , include
from django.conf import settings
from company.views import Company

urlpatterns = [
    path('about/', Company.as_view(), name='about' ),

]