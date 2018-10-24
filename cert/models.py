from django.db import models


# Create your models here.

cert_choices = ['IV', 'EV', 'OV', 'DV']


class Certificates(models.Model):
    issuer_common_name = models.CharField(max_length=200)
    issuer_organization = models.CharField(max_length=200)
    message = models.TextField()
    result_color_hex = models.CharField(max_length=100)
    subject_common_name = models.CharField(max_length=100)
    subject_organization = models.CharField(max_length=100)
    validation_result = models.CharField(max_length=100)
    validation_result_short = models.CharField(max_length=5)

