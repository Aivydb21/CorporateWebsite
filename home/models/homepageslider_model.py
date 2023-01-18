from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class HomePageSlider(models.Model):
    home = models.ForeignKey('home.HomePageContent',on_delete=models.CASCADE, null=True, blank=True)
    slider_image =models.ImageField(upload_to="slider/image")
    title = models.CharField(max_length=100)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "Home Page Slider"

    def __str__(self):
        return str(self.id)        