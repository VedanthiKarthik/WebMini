from django.db import models

# Create your models here.
class Courses(models.Model):
    
    title= models.CharField(max_length=100)
    description=models.TextField(null=True)
    price = models.FloatField(null=True, blank=True, default=None)
    rating= models.FloatField(null=True, blank=True, default=None)
    course_urls= models.CharField(null=True,max_length=200,default=None)

    
    # offer =models.BooleanField(default=False)
    # img= models.ImageField(_(""), upload_to='pics', height_field=None, width_field=None, max_length=None)