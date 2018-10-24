from django.db import models


# Create your models here.
class FeedbackData(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    webPage = models.CharField(max_length=100)
    subject = models.TextField(blank=True)
