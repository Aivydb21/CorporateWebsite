from django.forms import ModelForm
from contact.models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'query_type',
            'message',
        ]