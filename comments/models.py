from django.db import models

# Create your models here.

class Comments(models.Model):

    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    comment = models.TextField(verbose_name='کامنت')
    image = models.ImageField(upload_to='images/',verbose_name='عکس')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'

    def __str__(self):
        return self.name + ' - ' + str(self.is_active)
