from mission.models import MissionPage
from django.views import View
from django.shortcuts import render
from home.forms import NewsletterForm
from django.shortcuts import redirect
from home.models import Footer, HomePageContent
from utils import sendEmail
from services.models import ServicesParagraph
from django.http import JsonResponse
class Mission(View):
    def get(self,request):
        mission_content = MissionPage.objects.last()
        home_page_footer = Footer.objects.last()
        home_page_content = HomePageContent.objects.last()
        home_page_services = ServicesParagraph.objects.all()
        form = NewsletterForm()
        context = {}
        context['home_page_footer'] = home_page_footer
        context['mission_content'] = mission_content
        context['home_page_content'] = home_page_content
        context['home_page_services'] = home_page_services
        context['form'] = form
        return render(request , 'mission.html' , context)
    def post(self,request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            sendEmail(email,'',request)       
        return JsonResponse({'message': "Form submitted"}, status=200)