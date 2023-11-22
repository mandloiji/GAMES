from django.db import models
from tinymce.models import HTMLField


class Tech(models.Model):
    heading= HTMLField()
    description = HTMLField()
    image = models.ImageField(upload_to= 'off_img/')

class NewModel(models.Model):
    name = models.CharField(max_length=33)
    email = models.EmailField(max_length=33)
    phone = models.IntegerField (max_length=33)
    Device = models.CharField(max_length=33)



# Create your models here.
