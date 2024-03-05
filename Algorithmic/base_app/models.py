from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
# Create your models here.
