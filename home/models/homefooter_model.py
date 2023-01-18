from django.db import models
from ckeditor.fields import RichTextField

class Footer(models.Model):
    footer_logo = models.ImageField(upload_to="home/logo")
    footer_description = models.CharField(max_length=2000 )
    office_address  = models.CharField(max_length=2000 )
    phone_no        = models.CharField(max_length=1000)
    email           = models.EmailField()
    home = models.ForeignKey('home.HomePageContent',on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Footer'

    def __str__(self):
        return str(self.id)