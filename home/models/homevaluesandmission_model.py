from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html

class HomePageValueAndMissions(models.Model):
    home = models.ForeignKey('home.HomePageContent',on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to="home/valueandmission")
    title = models.CharField(max_length=100)
    description = RichTextField()

    class Meta:
        verbose_name_plural = 'Missions and Ideal Clients'


    def __str__(self):
        return str(self.id)