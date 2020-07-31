from django.shortcuts import render, redirect

#from .register import register
# Create your views here.
from register.models import SignUp
def register(request):

    if request.method == 'POST':
        email = request.POST.get('Email')
        name = request.POST.get('Name')
        contact = request.POST.get('Contact')
        hostel = request.POST.get('Hostel')
        room = request.POST.get('Room')
        pwd = request.POST.get('Password')

        print(name)
#        reg = register.objects.create_user(name=name, pwd=pwd, email=email, contact=contact, hostel=hostel, room=room)
#        reg.save();
        SignUp(name=name, contact=contact, email=email, pwd=pwd, hostel=hostel, room=room).save()

        return redirect('login')
    else:
        return render(request,'register.html')