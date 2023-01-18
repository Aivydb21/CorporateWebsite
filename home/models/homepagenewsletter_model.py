from django.db import models
from ckeditor.fields import RichTextField

class HomePageNewsLetter(models.Model):
    email = models.EmailField()
    created_at = models.DateField(auto_now=True,null=True, blank=True) 

    class Meta:
        verbose_name_plural = 'NewsLetter'

    def __str__(self):
        return str(self.id)