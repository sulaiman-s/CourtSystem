from codecs import backslashreplace_errors
from email.policy import default
from django.db import models

# Create your models here.


class MeetingRequest(models.Model):
    client_name = models.CharField(max_length=255, blank=False)
    lawyer_name = models.CharField(max_length=255, blank=False)
    meeting_type = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=False)
    meeting_Location = models.CharField(
        max_length=255, blank=False, default="")
    meeting_Status = models.CharField(max_length=255, default='pending')
    description = models.TextField(default='')


class Meetings(models.Model):
    client_name = models.CharField(max_length=255, blank=False)
    lawyer_name = models.CharField(max_length=255, blank=False)
    meeting_type = models.CharField(max_length=255, blank=True)
    meeting_Location = models.CharField(
        max_length=255, blank=False, default="")
    time = models.CharField(max_length=255, blank=False)
    description = models.TextField(default='')
