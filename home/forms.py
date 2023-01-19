from django.forms import ModelForm
from django import forms
from home.models import HomePageNewsLetter
class NewsletterForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'newsletter-input-field', 'placeholder':'john@example.com'}) , label='')
    class Meta:
        model = HomePageNewsLetter
        fields = ['email']