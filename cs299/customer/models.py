from calendar import EPOCH
from django.db import models
import datetime

# Create your models here.

class CustomerData(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    prefftime=models.TimeField()
    contact=models.CharField(max_length=122)
    bit=models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    
