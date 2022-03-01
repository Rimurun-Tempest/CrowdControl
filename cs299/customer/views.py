import re
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .models import CustomerData
from shopkeeper.models import ShopData
from datetime import datetime
from django.contrib import messages


# Create your views here.


def register(request: HttpRequest):
    Shop_list = ShopData.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        prefftime = request.POST['prefftime']
        phone = request.POST['number']
        s = ""
        for shop in Shop_list:
            try:
                request.POST[shop.name]
                s += '1'
            except MultiValueDictKeyError:
                s += '0'
        CustomerInfo = CustomerData(name=name, contact=phone, email=email,
                            prefftime=prefftime,bit=s, date=datetime.today())
        CustomerInfo.save()
        messages.success(request, 'Profile has been registered')

    return render(request, 'customer/register.html',
                  {'Shop_list': Shop_list})
