from django.shortcuts import render
from services.models import ServicesParagraph,ServicesPageBanner , HowItWorks
from django.views import View
from django.shortcuts import render
from home.forms import NewsletterForm
from django.shortcuts import redirect
from home.models import Footer, HomePageContent
from utils import sendEmail
from django.http import JsonResponse
# Create your views here.
class ServicesView(View):
    def get(self,request):
        services_banner = ServicesPageBanner.objects.last()
        services_paragraph = ServicesParagraph.objects.last()
        home_page_footer = Footer.objects.last()
        home_page_content = HomePageContent.objects.last()
        home_how_it_works = HowItWorks.objects.all()
        form = NewsletterForm()
        context = {}
        context['home_page_footer'] = home_page_footer
        context['services_banner'] = services_banner
        context['home_page_content'] = home_page_content
        context['services_paragraph'] = services_paragraph
        context['home_how_it_works'] = home_how_it_works
        
        context['form'] = form
        return render(request , 'services.html' , context)
    def post(self,request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            sendEmail(email,'',request)       
        return JsonResponse({'message': "Form submitted"}, status=200)    