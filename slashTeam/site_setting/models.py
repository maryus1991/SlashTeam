from django.db import models

# Create your models here.
class Site(models.Model):

    keywords_meta_tag = models.CharField(max_length=255)
    description_meta_tag = models.TextField()
    author_meta_tag = models.CharField(max_length=255)

    about_work_keywords = models.TextField()
    description_home = models.TextField()
    image = models.ImageField(upload_to='site_setting/images/')

    Team_email=models.CharField(max_length=255)
    Team_instagram=models.CharField(max_length=255)
    Team_telegram=models.CharField(max_length=255)


