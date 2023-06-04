from django.db import models
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=255)

    content_type = models.OneToOneField(ContentType, on_delete=models.SET_DEFAULT, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey()