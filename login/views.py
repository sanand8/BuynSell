from django.shortcuts import render, redirect
from register.models import SignUp
from django.contrib.sessions.models import Session
# Create your views here.
def logout(request):
    if request.session.has_key('username'):
        request.session.flush()

    p = 1
    return redirect('/',{'p':1})

def myprofile(request):
    username = request.Session.get('username')
    data = SignUp.objects.all()
    mail = 'a'
    name = 'a'
    contact = 1
    hostel = 'g'
    room = 1

    for d in data:
        if d.username == username:
            name = d.name
            mail = d.mail
            contact = d.contact
            hostel = d.hostel
            room = d.room
            return render(request,myprofile.html,{'mail':mail, 'name':name, 'contact':contact, 'hostel':hostel, 'room':room})

            
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
                request.session['username'] = d.username
                break
        if p == 1:
            return render(request,'home.html',{'name':naam, 'p':1, 'id':num})
        else:
            return redirect('login')
    
    else:
        return render(request,'login.html')