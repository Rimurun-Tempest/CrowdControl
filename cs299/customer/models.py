from calendar import EPOCH
from django.db import models
import datetime

# Create your models here.


class CustomerData(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    # prefftime=models.TimeField()
    # bit=models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


class QueryList(models.Model):
    user=models.ForeignKey(CustomerData,default=None,on_delete=models.CASCADE);
    prefftime1 = models.TimeField()
    prefftime2 = models.TimeField()
    prefftime3 = models.TimeField()
    bit = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.name
