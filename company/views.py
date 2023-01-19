from company.models import CompanyPage , CompanySectionOne, CompanySectionTwo, CompanySectionThree, CompanySectionFour, CompanySectionFive
from django.views import View
from django.shortcuts import render
from home.forms import NewsletterForm
from django.shortcuts import redirect
from home.models import Footer, HomePageContent
from utils import sendEmail
from services.models import ServicesParagraph
from django.http import JsonResponse
class Company(View):
    def get(self,request):
        company_content = CompanyPage.objects.last()
        company_section_one = CompanySectionOne.objects.last()
        company_section_two = CompanySectionTwo.objects.last()
        company_section_three = CompanySectionThree.objects.last()
        company_section_four = CompanySectionFour.objects.last()
        company_section_five = CompanySectionFive.objects.last()
        home_page_footer = Footer.objects.last()
        home_page_content = HomePageContent.objects.last()
        home_page_services = ServicesParagraph.objects.all()
        form = NewsletterForm()
        context = {}
        context['home_page_footer'] = home_page_footer
        context['company_content'] = company_content
        context['home_page_content'] = home_page_content
        context['home_page_services'] = home_page_services
        context['company_section_one'] = company_section_one
        context['company_section_two'] = company_section_two
        context['company_section_three'] = company_section_three
        context['company_section_four'] = company_section_four
        context['company_section_five'] = company_section_five
        
        context['form'] = form
        return render(request , 'company.html' , context)
    def post(self,request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            sendEmail(email,'',request)       
        return JsonResponse({'message': "Form submitted"}, status=200)