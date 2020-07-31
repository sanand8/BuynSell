from django.shortcuts import render, redirect
from register.models import SignUp

# Create your views here.
def logout(request):
    return redirect('/')

def login(request):
    if request.method == 'POST':

        mail = request.POST.get('Email')
        pswd = request.POST.get('Password')

        data = SignUp.objects.all()

        p = 0
        naam = "a"
        for d in data:
            if d.email == mail and d.pwd == pswd:
                print("verified")
                naam = d.name
                p = 1
                break
        if p == 1:
            return render(request,'home.html',{'name':naam, 'p':1})
        else:
            return redirect('login')
    
    else:
        return render(request,'login.html')