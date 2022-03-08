from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import CustomerData, QueryList
from shopkeeper.models import ShopData
from datetime import datetime
from django.contrib import messages

# Create your views here.


def register(request: HttpRequest):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        CustomerInfo = CustomerData(name=name, contact=phone, email=email,
                                    password=password, date=datetime.today())
        CustomerInfo.save()
        messages.success(request, 'Profile has been registered')

    return render(request, 'customer/register.html')


def profile(request):
    Shop_list = ShopData.objects.all()
    if request.method == "POST":
        preftime1 = request.POST['prefftime1']
        preftime2 = request.POST['prefftime2']
        preftime3 = request.POST['prefftime3']
        s = ""
        for shop in Shop_list:
            try:
                request.POST[shop.name]
                s += '1'
            except MultiValueDictKeyError:
                s += '0'
        CustomerQuery = QueryList(
            prefftime1=preftime1, prefftime2=preftime2, prefftime3=preftime3, bit=s)
        CustomerQuery.save()
        messages.success(request, 'Query has been sent!')
    return render(request, 'profile.html', {'Shop_list': Shop_list})


def CustomerLogin(request):
    if request.method == "POST":
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        User = CustomerData.objects.filter(name=userName, password=passWord)
        # print(User)
        if len(User) == 1:
            return redirect('profile')
            # check redirect yourself once
        else:
            return redirect('login')
    else:
        return render(request, 'customer/login.html')


# def CustomerLogout(request):
#     return redirect(request, 'home.html')
