from calendar import EPOCH
from django.db import models
import datetime

# Create your models here.


class ShopData(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    Opentime = models.TimeField()
    closetime = models.TimeField()
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name 
    

