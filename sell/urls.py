from django.urls import path, include
from . import views

urlpatterns = [
    path('sell',views.sell,name='sell')
]