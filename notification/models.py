from email import message
from pyexpat import model
from django.db import models

# Create your models here.


class Notification(models.Model):
    name = models.CharField(max_length=255, blank=False)
    token = models.CharField(max_length=255, blank=False)

class ClientNotification(models.Model):
    client_name=models.CharField(max_length=255,blank=False)
    message=models.CharField(max_length=255,blank=False)


class LawyerNotification(models.Model):
    lawyer_name=models.CharField(max_length=255,blank=False)
    message=models.CharField(max_length=255,blank=False)