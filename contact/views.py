from contact.models import Contact , ContactUs , ContactBanner
from django.views import View
from django.shortcuts import render
from contact.forms import ContactForm
from django.shortcuts import redirect
from home.models import Footer, HomePageContent
from utils import sendEmailContact
from services.models import ServicesParagraph
from django.http import JsonResponse

class ContactView(View):
    def get(self,request):
        contact = ContactUs.objects.last()
        home_page_footer = Footer.objects.last()
        contact_banner = ContactBanner.objects.last()
        home_page_services = ServicesParagraph.objects.all()
        home_page_content = HomePageContent.objects.last()
        form = ContactForm()
        context = {}
        context['home_page_footer'] = home_page_footer
        context['contact'] = contact
        context['home_page_content'] = home_page_content
        context['contact_banner'] = contact_banner
        context['home_page_services'] = home_page_services
        
        
        context['form'] = form
        return render(request , 'contact.html' , context)
    def post(self,request):
        print(request.POST, 'post')
        form = ContactForm(request.POST)
        print(form.errors, 'data')
        if form.is_valid():
            print('valid')
            obj = form.save()
            sendEmailContact(obj,'',request) 
        return JsonResponse({'message': "Form submitted"}, status=200)