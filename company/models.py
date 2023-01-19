from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class CompanyPage(models.Model):
    about_banner = models.ImageField(upload_to='about_banner/images')
    banner_title = models.CharField(max_length=100)
    
     
    
    def __str__(self):
        return self.banner_title

    class Meta:
        verbose_name_plural = 'About'

class CompanySectionOne(models.Model):        
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    about = models.ForeignKey(CompanyPage, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'About Section 1'  
class CompanySectionTwo(models.Model):
    
    heading = models.CharField(max_length=100)
    heading_description = RichTextField()
    image = models.ImageField(upload_to='about_section_1/images')  
    about = models.ForeignKey(CompanyPage, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'About Section 2'      
class CompanySectionThree(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    about = models.ForeignKey(CompanyPage, on_delete=models.CASCADE)
 

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'About Section 3' 

class CompanySectionFour(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    image = models.ImageField(upload_to='about_section_3/images')
    about = models.ForeignKey(CompanyPage, on_delete=models.CASCADE)
 

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'About Section 4' 

class CompanySectionFive(models.Model):
    title = models.CharField(max_length=100)
    title_description = RichTextField()
    about = models.ForeignKey(CompanyPage, on_delete=models.CASCADE)
 

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'About Section 5'         