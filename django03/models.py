from django.db import models

# Create your models here.

class wenzhang(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.title