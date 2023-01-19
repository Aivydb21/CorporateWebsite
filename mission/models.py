from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class MissionPage(models.Model):
    mission_banner = models.ImageField(upload_to='mission_banner/images')
    banner_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    mission_main_title = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='mission/images')
     
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Mission'

         