from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login as log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
# Create your views here.
def login(req):
    if req.GET:
        form = AuthenticationForm()
    if req.POST:  
        form = AuthenticationForm(request=req,data=req.POST)                                                                  
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request=req,username=username, password=password) 
        if user is not None:                              
            log(request=req,user=user)                                              
            messages.add_message(req,messages.SUCCESS,"خوش آمدید")                 
            return HttpResponseRedirect('')                                    
        else:
            messages.add_message(req,messages.ERROR,"مشخصات ورودی اشتباه است")                              
        
    return render(req,'pages/login.html',{'form':form})


def signup(req):
    cap = sinupForm()
    msg = ''
    if req.POST:
        cap = sinupForm(req.POST)
        if cap.is_valid():
            username = req.POST.get('username')
            password = req.POST.get('password')
            return HttpResponseRedirect('/')
        else:
            msg = "<h1>Invalid POST request</h1>"
            
            
    return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg})