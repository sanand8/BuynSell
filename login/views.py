from django.shortcuts import render, redirect
from register.models import SignUp

# Create your views here.
def logout(request):
    p = 1
    return redirect('/',{'p':1})

def login(request):
    if request.method == 'POST':

        mail = request.POST.get('Email')
        pswd = request.POST.get('Password')

        data = SignUp.objects.all()

        p = 0
        naam = "a"
        num = 1
        for d in data:
            if d.email == mail and d.pwd == pswd:
                print("verified")
                naam = d.name
                p = 1
                num = d.id
                break
        if p == 1:
            return render(request,'home.html',{'name':naam, 'p':1, 'id':num})
        else:
            return redirect('login')
    
    else:
        return render(request,'login.html')