from django.db import models
from django.contrib.auth.models import User


class Shopkeeper(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=256,blank=False,default="")
    shop_bio = models.TextField(blank=False,default="")
    type = models.CharField(max_length=256,blank=False)
    is_customer = models.BooleanField(default=False,editable=False)
    capacity = models.IntegerField(null=True)
    opening_time = models.TimeField(null=True)
    closing_time = models.TimeField(null=True)
    
    def __str__(self):
        return self.user.first_name    
