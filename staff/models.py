from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=255)