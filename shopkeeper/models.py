from django.db import models
from django.contrib.auth.models import User


class Shopkeeper(models.Model):
    shopkeeper = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=256,blank=False)
    is_customer = models.BooleanField(default=False)
    capacity = models.IntegerField(blank=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    