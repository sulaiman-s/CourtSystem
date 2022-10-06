from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Lawyer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ph_no = models.CharField(max_length=255, blank=False, default="")
    gender = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=False, default='none')
    is_registered = models.BooleanField(default=False)
    doc_image = models.ImageField(upload_to="lawyerDocs", blank=True)


class User(AbstractUser):
    location = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    ph_no = models.CharField(max_length=255, blank=False, default="")


class ProfilePic(models.Model):
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profiles', blank=False)
