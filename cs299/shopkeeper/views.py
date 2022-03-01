from django.shortcuts import render
from datetime import datetime
from shopkeeper.models import ShopData
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        Opentime = request.POST['opentime']
        closetime = request.POST['closetime']
        ShopInfo = ShopData(name=name, phone=phone, email=email,
                            Opentime=Opentime, closetime=closetime, date=datetime.today())
        ShopInfo.save()
        messages.success(request, 'Profile has been reigstered')
    return render(request, 'shopkeeper/register.html')
