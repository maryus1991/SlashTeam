from django.db import models

# Create your models here.
class Site(models.Model):

    keywords_meta_tag = models.CharField(max_length=255, verbose_name='واژهای متا تگ')
    description_meta_tag = models.TextField(verbose_name='توضیحات متا تگ')
    author_meta_tag = models.CharField(max_length=255,verbose_name='نویسنده متا تگ')

    about_work_keywords = models.TextField(verbose_name='درباره کار (واژه ها و با , اسپلبت کن )')
    description_home = models.TextField(verbose_name='توضیحات صفحه اصلی')
    image = models.ImageField(upload_to='site_setting/images/',verbose_name='عکس صفحه اصلی')

    class Meta:
        verbose_name='تنظیمات'
        verbose_name_plural='تنظیمات'

