from django.urls import path,include
from . import views

app_name='shopkeeper'

urlpatterns=[
    path('',views.index, name='shopkeeper'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.userLogout,name='logout'), 
    path('profile/',views.profile,name="profile"),
    path('settings/',views.settings, name='settings'),   
]