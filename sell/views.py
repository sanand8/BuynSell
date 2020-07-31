from django.shortcuts import render,redirect
from sell.models import Sell
# Create your views here.
def sell(request):
    if request.method == 'POST':
        img = request.POST.get('Img')
        price = request.POST.get('Price')
        contact = request.POST.get('Contact')
        des = request.POST.get('Description')
        Sell(img=img, price=price, contact=contact, description=des).save()
        return redirect('/')
    else:
        return render(request,'sell.html')