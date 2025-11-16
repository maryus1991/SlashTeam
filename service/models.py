from django.db import models

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=100, verbose_name='نام مهارت')
    value = models.TextField(verbose_name='مقدار')
        
    class Meta:
        verbose_name='خدمت'
        verbose_name_plural='خدمات'
    
