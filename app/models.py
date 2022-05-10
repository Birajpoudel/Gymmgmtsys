from django.db import models

#Banners
class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)



# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()