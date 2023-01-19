from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query_type = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    contacted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = "Contact Us Form"
        verbose_name_plural = "Contact Us Form"

class ContactUs(models.Model):

    contact_us_title = models.CharField(max_length=255,verbose_name='Title')

    def __str__(self):
        return str(self.contact_us_title)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

class ContactBanner(models.Model):
    contact = models.ForeignKey(ContactUs, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255,verbose_name='Banner Title')
    banner = models.ImageField(upload_to="contact_banner/image")
    
    class Meta:
        verbose_name = "Contact Banner"
        verbose_name_plural = "Contact Banner"

    def __str__(self):
        return str(self.id) 

    