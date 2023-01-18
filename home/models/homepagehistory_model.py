from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html 
class HomePageHistory(models.Model):
    home = models.ForeignKey('home.HomePageContent',on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="history/image") 
    
    class Meta:
        verbose_name_plural = 'About'



    def __str__(self):
        return str(self.id)

