from django.db import models

# Create your models here.

class Contacts(models.Model):

    name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن')

    class Meta:
        verbose_name='تماس'
        verbose_name_plural='تماس ها'
    
