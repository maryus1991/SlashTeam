from django.db import models

# Create your models here.

class Members(models.Model):

    name = models.CharField(verbose_name= 'نام', max_length=100)
    skills = models.TextField(verbose_name='مهارت ها', max_length=250)
    website = models.URLField(verbose_name='لینک سایت', null=True, blank=True)
    telegram = models.URLField(verbose_name='لینک تلگرام', null=True, blank=True)
    whatsapp = models.URLField(verbose_name='لینک واتساپ', null=True, blank=True )
    photo = models.ImageField(upload_to='members/',verbose_name='عکس')

    class Meta:
        verbose_name='عضو'
        verbose_name_plural='اعضا'

    def __str__(self):
        return self.name
    

