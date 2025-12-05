from django.db import models

# Create your models here.

class About(models.Model):
    about = models.TextField(
        verbose_name='درباره ما',
    )
    class Meta:
        verbose_name='درباره'
        verbose_name_plural='درباره'

    def __str__(self):
        return str(self.id)
    
