from django.urls import path
from customer import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('profile',views.profile,name='profile'),
    path('login', views.CustomerLogin, name='login')
    # path('logout', views.CustomerLogout, name='logout')
]

