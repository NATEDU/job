from django.db import models

class Allip(models.Model):
    all_ip = models.CharField(max_length=30)
    
  