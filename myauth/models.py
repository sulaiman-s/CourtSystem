from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Lawyer(models.Model):
      username=models.CharField(max_length=255,unique=True)
      email=models.CharField(max_length=255,unique=True)
      password=models.CharField(max_length=255)
      location=models.CharField(max_length=255)
      gender=models.CharField(max_length=255,blank=True)
      is_registered=models.BooleanField(default=False)
      doc_image=models.ImageField(upload_to="lawyerDocs",blank=True)

class User(AbstractUser):
    location = models.CharField(max_length=255,blank=True)
    gender=models.CharField(max_length=255,blank=True)
