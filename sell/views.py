from django.shortcuts import render,redirect
from sell.models import Sell
# Create your views here.
def sell(request):
    if request.method == 'POST':
        img = request.POST.get('Img')
        price = request.POST.get('Price')
        contact = request.POST.get('Contact')
        des = request.POST.get('Description')
        username = request.session.get('username','')
        Sell(img=img, price=price, contact=contact, description=des, username=username).save()
        return render(request,'home.html',{'name':username})
    else:
        return render(request,'sell.html')