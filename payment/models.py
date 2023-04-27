from django.db import models

# Create your models here.
amount = models.DecimalField(max_digits=9, decimal_places=2)
payment_date = models.DateTimeField()
payment_type = models.CharField(max_length=255)