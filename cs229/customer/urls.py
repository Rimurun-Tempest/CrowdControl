from django.contrib import admin
from django.urls import path, include
from customer import views

urlpatterns = [
    path('register', views.register, name='register')
]
