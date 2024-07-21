from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as log,logout as logt
from django.contrib.auth.models import User
from pixel.models import users,Accounts as ac
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.mail import send_mail


# Create your views here.
def login(req):
    if req.POST:                                                                 
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(request=req,username=username, password=password) 
        if user is not None:                              
            log(request=req,user=user)                                              
            messages.add_message(req,messages.SUCCESS,"خوش آمدید")                 
            return HttpResponseRedirect('/')                                    
        else:
            messages.add_message(req,messages.ERROR,"مشخصات ورودی اشتباه است")                              
        
    return render(req,'pages/login.html',)


def signup(req):
    cap = sinupForm()
    msg = ''
    type_data = ''
    if req.POST:
        cap = sinupForm(data=req.POST)
        if cap.is_valid():
            username = cap.cleaned_data['username']
            password = cap.cleaned_data['password']
            type_data = type(cap.cleaned_data['username'])
            if password == cap.cleaned_data['password2']:
                #if cap.cleaned_data['tellnumber'].isdigit():
                    User.objects.create_user(username=username,password=password,email=cap.cleaned_data['email']
                                             ,)
                    users.objects.create(
                        username=username,
                        password=User.objects.get(username=username),
                        email=cap.cleaned_data['email'],
                        fname=cap.cleaned_data['fname'],
                        lname=cap.cleaned_data['lname'],
                        codeacc = ac.objects.get(id=2),
                        tellNumber=cap.cleaned_data['tellnumber'],
                        location=cap.cleaned_data['location'],
                        birthday=cap.cleaned_data['birthday'],
                        about=cap.cleaned_data['subject'],
                        education=cap.cleaned_data['education'],
                        langs=cap.cleaned_data['langs'],
                        t_p=cap.cleaned_data['t_p'],
                        cod_posti=cap.cleaned_data['cod_posti'],
                        age=1
                        
                    )
                  
            
    return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg,'type':type_data})

@login_required
def logout(req):
    if req.user.is_authenticated:
        logt(req)
    return redirect('/')

def send_email(req,email):
    import random as r
    abscode = r.randint(1000000,9999999)
    send_mail(
    f"code is '{abscode}'",
    "signup code by mohsen ♥.",
    email,
    [email],
    fail_silently=False,
)
    return HttpResponse('<h2>SENDING Message</h2>')
    