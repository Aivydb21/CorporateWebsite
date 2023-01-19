from ourclient.models import ClientPageBanner , ClientPageSectionOne, ClientPageSectionThree, ClientsHowItWorks, ClientPageSectionFour
from django.views import View
from django.shortcuts import render
from home.forms import NewsletterForm
from django.shortcuts import redirect
from home.models import Footer, HomePageContent
from utils import sendEmail
from services.models import ServicesParagraph
from django.http import JsonResponse

class OurClients(View):
    def get(self,request):
        client_banner = ClientPageBanner.objects.last()
        client_section_one = ClientPageSectionOne.objects.last()
        client_section_three = ClientPageSectionThree.objects.last()
        client_how_it_work = ClientsHowItWorks.objects.all()
        client_section_four = ClientPageSectionFour.objects.last()
        home_page_footer = Footer.objects.last()
        home_page_content = HomePageContent.objects.last()
        home_page_services = ServicesParagraph.objects.all()
        form = NewsletterForm()
        context = {}
        context['home_page_footer'] = home_page_footer
        context['client_banner'] = client_banner
        context['home_page_content'] = home_page_content
        context['home_page_services'] = home_page_services
        context['client_section_one'] = client_section_one
        context['client_section_three'] = client_section_three
        context['client_how_it_work'] = client_how_it_work
        context['client_section_four'] = client_section_four
        
        context['form'] = form
        return render(request , 'clients.html' , context)
    def post(self,request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            sendEmail(email,'',request)       
        return JsonResponse({'message': "Form submitted"}, status=200)