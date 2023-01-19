from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ClientPageBanner(models.Model):
    banner_image = models.ImageField(upload_to='client_banner/images')
    title = models.CharField(max_length=100)
    how_it_work_title = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Our Client"

    def __str__(self):
        return str(self.title)

class ClientPageSectionOne(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    client = models.ForeignKey(ClientPageBanner,on_delete=models.CASCADE,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Section 1"

    def __str__(self):
        return str(self.id)

class ClientsHowItWorks(models.Model):
    icon = models.ImageField(upload_to="home/customer_love")
    text = models.CharField(max_length=250)
    client = models.ForeignKey(ClientPageBanner,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'How It Works'


    def __str__(self):
        return str(self.id)      


class ClientPageSectionThree(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    client = models.ForeignKey(ClientPageBanner,on_delete=models.CASCADE,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Section 3"

    def __str__(self):
        return str(self.id)        

class ClientPageSectionFour(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    image = models.ImageField(upload_to='client-section-2/images')
    client = models.ForeignKey(ClientPageBanner,on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        verbose_name_plural = "Section 4"

    def __str__(self):
        return str(self.id)