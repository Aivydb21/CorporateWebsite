from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html

class HomePageContent(models.Model):
    logo = models.ImageField(upload_to="home/logo") 
    newsletter_title = models.CharField(max_length=100)
    newsletter_description= models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Home Page "
    
    