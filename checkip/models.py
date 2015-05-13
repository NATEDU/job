from django.db import models

# Create your models here.
class check_all_ip(models.Model):

    ip= models.CharField(max_length=30)
    test_ip = models.BooleanField()
