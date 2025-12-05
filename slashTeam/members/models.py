from django.db import models

# Create your models here.

class Members(models.Model):

    name = models.CharField(verbose_name='نام')
    skills = models.TextField(verbose_name='مهارت ها')
    website = models.URLField(verbose_name='لینک سایت')
    telegram = models.URLField(verbose_name='لینک تلگرام')
    whatsapp = models.URLField(verbose_name='لینک واتساپ')
    photo = models.ImageField(upload_to='members/',verbose_name='عکس')

    class Meta:
        verbose_name='عضو'
        verbose_name_plural='اعضا'

    def __str__(self):
        return self.name
    

