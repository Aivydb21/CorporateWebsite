from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class ServicesPageBanner(models.Model):
    banner_image = models.ImageField(upload_to='services_banner/images')
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return str(self.id)



 
class ServicesParagraph(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    event_services = models.ForeignKey(ServicesPageBanner, on_delete=models.CASCADE,blank=True)
    class Meta:
        verbose_name_plural = 'Paragraphs'
    def __str__(self):
        return str(self.id)

class HowItWorks(models.Model):
    icon = models.ImageField(upload_to="home/customer_love")
    text = models.CharField(max_length=250)
    services = models.ForeignKey(ServicesPageBanner,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'How It Works'


    def __str__(self):
        return str(self.id)        