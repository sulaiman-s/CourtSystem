from django.db import models

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=255, blank=False)
    lawyer_name = models.CharField(max_length=255, blank=False)
