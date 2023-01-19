from home.models import HomePageContent, HomePageNewsLetter , HomePageSlider, \
    HomePageValueAndMissions, HomePageHistory, Footer  
from services.models import ServicesParagraph
from ourclient.models import ClientsHowItWorks , ClientPageBanner
from django.views import View
from django.shortcuts import render
from home.forms import NewsletterForm
from django.shortcuts import redirect
from utils import sendEmail
from django.contrib import messages
from django.http import JsonResponse, HttpResponse


class Home(View):

    def get(self,request):
        print('get')
        home_page_content = HomePageContent.objects.all().last()
        home_page_values_and_mission = HomePageValueAndMissions.objects.all()
        home_page_slider = HomePageSlider.objects.all()
        home_page_services = ServicesParagraph.objects.all()
        home_page_history = HomePageHistory.objects.all().last()
        client_how_it_work = ClientsHowItWorks.objects.all()
        client_banner = ClientPageBanner.objects.last()
        home_page_footer = Footer.objects.all().last()
        
        form = NewsletterForm()
        context = {}
        context['home_page_content'] = home_page_content
        context['home_page_values_and_mission']  = home_page_values_and_mission
        context['home_page_slider'] = home_page_slider
        context['home_page_services']  = home_page_services
        context['home_page_history'] = home_page_history
        context['home_page_footer'] = home_page_footer
        context['client_how_it_work'] = client_how_it_work
        context['client_banner'] = client_banner
        
        
        context['form'] = form
        return render(request , 'index.html' , context)

    def post(self,request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            sendEmail(email,'',request)       
        return JsonResponse({'message': "Form submitted"}, status=200)
        
