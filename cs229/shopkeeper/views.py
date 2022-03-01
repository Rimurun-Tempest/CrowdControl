from django.shortcuts import render
from datetime import datetime
from shopkeeper.models import ShopData

# Create your views here.


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('number')
        email = request.POST.get('email')
        Opentime = request.POST.get('opentime')
        closetime = request.POST.get('closetime')
        ShopInfo = ShopData(name=name, phone=phone, email=email,
                            Opentime=Opentime, closetime=closetime, date=datetime.today())
        ShopInfo.save()
    return render(request, 'shopkeeper/register.html')
