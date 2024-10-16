from django.db import models
from django.utils import timezone
import random
import string

def short_link_generetor(length:int=6):
    
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



class Url(models.Model):
    url = models.URLField()
    short_link = models.CharField(max_length=10, unique=True, default=short_link_generetor)
    
    created = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.url} -> {self.short_link}"
    
    
    class Meta:
        ordering = ['-created']
        
        indexes = [
            models.Index(fields=['-created'])
        ]