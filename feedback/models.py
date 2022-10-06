from django.db import models

# Create your models here.


class FeedBack(models.Model):
    username = models.CharField(max_length=255, blank=False)
    lawyer_name = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False)
    star_ratings = models.IntegerField(blank=True)
