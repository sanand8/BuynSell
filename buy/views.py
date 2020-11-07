from django.shortcuts import render
from sell.models import Sell

from django.conf import settings
# Create your views here.

def buy(request):
    sell = Sell.objects.all()
    return render(request,'buy.html',{'sell':sell})