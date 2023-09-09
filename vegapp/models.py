from django.db import models

# Create your models here.
class recform(models.Model):
    rec_name=models.CharField(max_length=100)
    rec_dec=models.CharField(max_length=100)
    rec_img=models.ImageField(upload_to="recipe")