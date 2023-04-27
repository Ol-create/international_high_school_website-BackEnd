from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()