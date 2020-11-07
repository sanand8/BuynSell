from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('logout',views.logout,name='logout'),
    path('sell/',include('sell.urls')),
    path('register/',include('register.urls')),
    path('buy/',include('buy.urls')),
    
]