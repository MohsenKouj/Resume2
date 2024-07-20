from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login as log
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from .forms import *
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
    if req.POST:
        cap = sinupForm(data=req.POST)
        if cap.is_valid():
            username = req.POST.get('username')
            password = req.POST.get('password')
            form = UserCreationForm(req.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            msg = "<h1>Invalid POST request</h1>"
            
            
    return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg})