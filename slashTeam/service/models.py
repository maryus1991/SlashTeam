from django.db import models

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=100, verbose_name='نام مهارت')
    value = models.TextField(verbose_name='مقدار')#
    service_icon = models.URLField(verbose_name='لینک ایکون', blank=True, null=True)
        
    class Meta:
        verbose_name='خدمت'
        verbose_name_plural='خدمات'

    def __str__(self):
        return self.name + '<+>' + self.value
