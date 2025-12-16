from django.db import models

# Create your models here.

class About(models.Model):
    about = models.TextField()


    def __str__(self):
        return str(self.id)
    
